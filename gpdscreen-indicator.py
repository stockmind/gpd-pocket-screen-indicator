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
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'GPDScreenManager'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('icons/screen-rotation-button-white.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    # Rotate landscape
    item_landscape = gtk.MenuItem('Rotate landscape')
    item_landscape.connect('activate', landscape)
    menu.append(item_landscape)

    # Rotate portrait
    item_portrait = gtk.MenuItem('Rotate Portrait')
    item_portrait.connect('activate', portrait)
    menu.append(item_portrait)

    # Restore display size
    item_portrait = gtk.MenuItem('Restore display size')
    item_portrait.connect('activate', displaysize)
    menu.append(item_portrait)

    # Quit 
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()

def landscape(source):
    gpdtouch landscape

def portrait(source):
    gpdtouch potrait

def dispaysize(source):
    gpdtouch displaysize

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()