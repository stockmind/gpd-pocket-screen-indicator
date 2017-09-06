#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# __author__ = "Simone Roberto Nunzi aka Stockmind"
# __copyright__ = "Copyright 2017"
# __credits__ = ["Timur Rubeko"]
# __license__ = "GPL"
# __version__ = "3.0"
# Icon used: https://www.flaticon.com/free-icon/screen-rotation-button_61030
# Icon author link: https://www.flaticon.com/authors/google

import os
import time
import signal
from subprocess import call

desktop = os.getenv("XDG_CURRENT_DESKTOP")                                     
is_unity = (desktop.lower() == "unity")    
is_kde = (desktop.lower() == "kde")    

print desktop

if is_unity:
    import gi
    gi.require_version('Gtk', '3.0')
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import Gtk as gtk
    from gi.repository import AppIndicator3 as appindicator
    
if not is_unity:
    from PyQt4 import QtGui

APPINDICATOR_ID = 'GPDScreenManager'

def main():
    if is_unity:
        indicator = appindicator.Indicator.new(APPINDICATOR_ID, get_resource_path('icons/screen-rotation-button-white.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        menu = buid_menu()
        indicator.set_menu(menu)
        gtk.main()
    if not is_unity:
        indicator = QtGui.QApplication([])
        icon = QtGui.QSystemTrayIcon(QtGui.QIcon(get_resource_path('icons/screen-rotation-button-white.svg')), indicator)
        menu = build_menu()
        icon.setContextMenu(menu)
        icon.show()
        indicator.exec_()

def build_menu():
    if is_unity:
        menu = gtk.Menu()

        # Rotate landscape
        item_landscape = gtk.ImageMenuItem('Rotate landscape')
        item_icon = gtk.Image()
        item_icon.set_from_file(get_resource_path('icons/tablet-with-blank-screen-white.svg'))
        item_landscape.set_image(item_icon)
        item_landscape.set_always_show_image(True)
        item_landscape.connect('activate', landscape)
        menu.append(item_landscape)
    
        # Rotate portrait
        item_portrait = gtk.ImageMenuItem('Rotate portrait')
        item_icon = gtk.Image()
        item_icon.set_from_file(get_resource_path('icons/cell-phone-with-blank-screen-white.svg'))
        item_portrait.set_image(item_icon)
        item_portrait.set_always_show_image(True)
        item_portrait.connect('activate', portrait)
        menu.append(item_portrait)
    
        # Restore display size
        #item_displaysize = gtk.MenuItem('Restore display size')
        #item_displaysize.connect('activate', displaysize)
        #menu.append(item_displaysize)
    
        # Restore display size
        item_resettouch = gtk.ImageMenuItem('Reset touchscreen')
        item_icon = gtk.Image()
        item_icon.set_from_file(get_resource_path('icons/synchronization-arrows-white.svg'))
        item_resettouch.set_image(item_icon)
        item_resettouch.set_always_show_image(True)
        item_resettouch.connect('activate', resettouch)
        menu.append(item_resettouch)
    
        # Quit
        item_quit = gtk.ImageMenuItem('Quit')
        item_quit.connect('activate', quit)
        menu.append(item_quit)
    
        menu.show_all()
        
    if not is_unity:
        menu = QtGui.QMenu()
        
        menu.addAction("Quit", QtGui.qApp.quit)

    return menu

def quit(source):
    gtk.main_quit()

def landscape(source):
    call(["gpdtouch", "landscape"])

def portrait(source):
    call(["gpdtouch", "portrait"])

def displaysize(source):
    call(["gpdtouch", "displaysize"])

def resettouch(source):
    call(("gksudo -- bash -c 'modprobe -r goodix; sleep 3; modprobe goodix'"), shell=True)

def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource    

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
