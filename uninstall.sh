#!/bin/bash

# Clean previous version of scripts
rm -f /etc/X11/Xsession.d/90-touch
rm -f /etc/X11/xinit/xinitrc.d/90-touch
systemctl stop gpdtouch.service
systemctl stop gpdtouch-wake.service
systemctl disable gpdtouch.service
systemctl disable gpdtouch-wake.service
rm -f /etc/systemd/system/gpdtouch.service
rm -f /etc/systemd/system/gpdtouch-wake.service
rm -f /usr/local/sbin/gpdtouch
rm -f /lib/systemd/system-sleep/gpdtouch

# Clean latest version of scripts
rm -f /etc/X11/Xsession.d/90-gpdscreen
rm -f /etc/X11/Xsession.d/99-gpdscreen-indicator
rm -f /etc/X11/xinit/xinitrc.d/90-gpdscreen
rm -f /usr/local/sbin/gpdscreen

rm -f gpdscreen /lib/systemd/system-sleep/gpdscreen

systemctl stop gpdscreen.service
systemctl stop gpdscreen-wake.service
systemctl disable gpdscreen.service
systemctl disable gpdscreen-wake.service
rm -f gpdscreen.service /etc/systemd/system/gpdscreen.service
rm -f gpdscreen-wake.service /etc/systemd/system/gpdscreen-wake.service

rm -f /usr/local/sbin/gpdscreen-indicator

rm -f /etc/X11/Xsession.d/99-gpdscreen-indicator

# Uninstall icons
rm -fr /usr/local/share/gpdscreen-indicator
