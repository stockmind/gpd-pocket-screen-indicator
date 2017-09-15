# GPD Pocket screen rotation utility

With this utility and traybar indicator you can easily manage screen and touch rotation of your device.

You can also switch from High DPI to Normal DPI mode to work easily on attached monitors at native DPI on Xorg.

I'm experimenting other features that may be added soon.

# Install

## Required dependencies

 ### Debian, Ubuntu, etc...:

	 - python
	 - python-gi
	 - gksu
	 - gir1.2-appindicator3-0.1

 ### Arch:

 	- gobject-introspection
 	- python2
 	- python2-gobject
 	- gksu

 ## GNOME-Shell Users

 	Gnome users must install an extension for Gnome Shell (Choose one):

 		- https://extensions.gnome.org/extension/1031/topicons/
 		- https://extensions.gnome.org/extension/495/topicons/

 	This extensions will enable legacy tray icons on top bar.

## Clone repository and run as root

    sudo ./install.sh

This will install gpdscreen rotation scripts, daemons and icons.

Reboot after install is required.

# Uninstall

Clone repository and run as root

    sudo ./uninstall.sh

This will also remove old versions of my gpdtouch scripts. 

# Credits

Base rotation script and daemons is based on initial bash work of chrisawcom 

Contributions by beeftornado, maxengel

Icons used: [Material Design by Google](https://www.flaticon.com/authors/google)
