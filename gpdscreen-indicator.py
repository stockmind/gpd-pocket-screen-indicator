#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# __author__ = "Simone Roberto Nunzi aka Stockmind"
# __copyright__ = "Copyright 2017"
# __credits__ = ["Timur Rubeko for initial daemon setup"]
# __license__ = "GPL"
# __version__ = "3.0"
# Icon used: https://www.flaticon.com/free-icon/screen-rotation-button_61030
# Icon author link: https://www.flaticon.com/authors/google

import os
import time
import signal
from subprocess import call

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'GPDScreenManager'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, get_resource_path('/usr/local/share/gpdscreen-indicator/icons/screen-rotation-button-white.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    menu = build_menu()
    indicator.set_menu(menu)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    # Rotate landscape
    item_landscape = gtk.ImageMenuItem('Rotate landscape')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/tablet-with-blank-screen-white.png'))
    item_landscape.set_image(item_icon)
    item_landscape.set_always_show_image(True)
    item_landscape.connect('activate', landscape)
    menu.append(item_landscape)

    # Rotate portrait
    item_portrait = gtk.ImageMenuItem('Rotate portrait')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/cell-phone-with-blank-screen-white.png'))
    item_portrait.set_image(item_icon)
    item_portrait.set_always_show_image(True)
    item_portrait.connect('activate', portrait)
    menu.append(item_portrait)
    
    # Rotate inverted portrait
    item_portrait = gtk.ImageMenuItem('Rotate inverse portrait')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/cell-phone-with-blank-screen-white.png'))
    item_portrait.set_image(item_icon)
    item_portrait.set_always_show_image(True)
    item_portrait.connect('activate', invertedportrait)
    menu.append(item_portrait)    

    # Restore display size
    #item_displaysize = gtk.MenuItem('Restore display size')
    #item_displaysize.connect('activate', displaysize)
    #menu.append(item_displaysize)

    # Restore display size
    item_resettouch = gtk.ImageMenuItem('Reset touchscreen')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/synchronization-arrows-white.png'))
    item_resettouch.set_image(item_icon)
    item_resettouch.set_always_show_image(True)
    item_resettouch.connect('activate', resettouch)
    menu.append(item_resettouch)

    # Normal DPI
    item_normaldpi = gtk.ImageMenuItem('Normal DPI')
    item_normaldpi.connect('activate', normaldpi)
    menu.append(item_normaldpi)

    # High DPI
    item_highdpi = gtk.ImageMenuItem('High DPI')
    item_highdpi.connect('activate', highdpi)
    menu.append(item_highdpi)

    # Quit
    item_quit = gtk.ImageMenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    
    return menu

def quit(*source):
    gtk.main_quit()

def landscape(*source):
    call(["gpdscreen", "landscape"])

def portrait(*source):
    call(["gpdscreen", "portrait"])
    
def invertedportrait(*source):
    call(["gpdscreen", "invertedportrait"])    

def displaysize(*source):
    call(["gpdscreen", "displaysize"])

def resettouch(*source):
    call(("gksudo -- gpdscreen touchreset"), shell=True)

def highdpi(*source):
    call(["gpdscreen", "highdpi"])

def normaldpi(*source):
    call(["gpdscreen", "normaldpi"])

def get_resource_path(rel_path):
    #dir_of_py_file = os.path.dirname(__file__)
    #rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    #abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    #return abs_path_to_resource    
    return rel_path

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
