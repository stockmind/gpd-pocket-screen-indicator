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
import ConfigParser

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'GPDScreenManager'
configfile = "/etc/gpdscreen-indicator/config"
Config = ConfigParser.ConfigParser()

def getconfig(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def setconfig(section,key,value):
    Config.set(section,key,value)
    with open(configfile, 'wb') as file:
        config.write(file)

def main():
    # Read config
    Config.read(configfile)
    maincolor = getconfig("icons")['maincolor'] # white - black
    menucolor = getconfig("icons")['menucolor'] # white - black

    if maincolor = None:
        maincolor = "white"

    if menucolor = None:
        menucolor = "white"

    # Init indicator
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, get_resource_path('/usr/local/share/gpdscreen-indicator/icons/screen-rotation-button-{}.svg'.format(maincolor)), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    menu = build_menu()
    indicator.set_menu(menu)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    # Rotate landscape
    item_landscape = gtk.ImageMenuItem('Rotate landscape')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/tablet-with-blank-screen-{}.svg'.format(menucolor)))
    item_landscape.set_image(item_icon)
    item_landscape.set_always_show_image(True)
    item_landscape.connect('activate', landscape)
    menu.append(item_landscape)

    # Rotate portrait
    item_portrait = gtk.ImageMenuItem('Rotate portrait')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/cell-phone-with-blank-screen-{}.svg'.format(menucolor)))
    item_portrait.set_image(item_icon)
    item_portrait.set_always_show_image(True)
    item_portrait.connect('activate', portrait)
    menu.append(item_portrait)
    
    # Rotate inverted portrait
    item_portrait = gtk.ImageMenuItem('Rotate inverse portrait')
    item_icon = gtk.Image()
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/cell-phone-with-blank-screen-{}.svg'.format(menucolor)))
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
    item_icon.set_from_file(get_resource_path('/usr/local/share/gpdscreen-indicator/icons/synchronization-arrows-{}.svg'.format(menucolor)))
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

    # Preferences menu
    preferencesmenu = gtk.Menu()
    item_preferences = gtk.ImageMenuItem('Preferences')
    item_preferences.set_submenu(preferencesmenu)
        # Theme White
        item_preferences_themewhite = gtk.ImageMenuItem('White Theme')
        item_preferences_themewhite.connect('activate', themewhite)
        preferencesmenu.append(item_preferences_themewhite)
        # Theme Black
        item_preferences_themeblack = gtk.ImageMenuItem('Black Theme')
        item_preferences_themeblack.connect('activate', themeblack)
        preferencesmenu.append(item_preferences_themeblack)
    menu.append(item_preferences)

    # Quit
    item_quit = gtk.ImageMenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    
    return menu

def quit(*source):
    Config.quit()
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

def themewhite(*source):
    setconfig("icons","maincolor","white")
    setconfig("icons","menucolor","white")
    call(["gpdscreen-indicator"])
    Config.quit()
    gtk.main_quit()

def themeblack(*source):
    setconfig("icons","maincolor","black")
    setconfig("icons","menucolor","black")
    call(["gpdscreen-indicator"])
    Config.quit()
    gtk.main_quit()


def get_resource_path(rel_path):
    #dir_of_py_file = os.path.dirname(__file__)
    #rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    #abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    #return abs_path_to_resource    
    return rel_path

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
