#!/bin/bash

cp gpdscreen-indicator.py /usr/local/sbin/gpdscreen-indicator
chmod +x /usr/local/sbin/gpdscreen-indicator

cp 99-gpdscreen-indicator /etc/X11/Xsession.d/99-gpdscreen-indicator

chmod +x /etc/X11/Xsession.d/99-gpdscreen-indicator

mkdir -p /usr/local/share/gpdscreen-indicator/icons
cp icons/*.png /usr/local/share/gpdscreen-indicator/icons/
