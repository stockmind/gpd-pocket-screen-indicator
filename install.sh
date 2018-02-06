#!/bin/bash

# Clean previous version of script
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
rm -f /etc/X11/Xsession.d/99-gpdscreen-indicator


# Copy xsession scripts for utility launch
cp xsession/90-gpdscreen /etc/X11/Xsession.d/90-gpdscreen
#cp xsession/99-gpdscreen-indicator /etc/X11/Xsession.d/99-gpdscreen-indicator
cp xsession/gpdscreen-indicator.desktop /etc/xdg/autostart/gpdscreen-indicator.desktop

chmod 0644 /etc/X11/Xsession.d/90-gpdscreen
#chmod 0644 /etc/X11/Xsession.d/99-gpdscreen-indicator
chmod 0644 /etc/xdg/autostart/gpdscreen-indicator.desktop

# Add rotate script for GDM login script
mkdir -p /etc/X11/xinit/xinitrc.d/
cp xsession/90-gpdscreen /etc/X11/xinit/xinitrc.d/90-gpdscreen
chmod 0644 /etc/X11/xinit/xinitrc.d/90-gpdscreen

# Add touchscreen rotation daemon for login screens and wayland
cp daemons/gpdscreen.sh /usr/local/sbin/gpdscreen
chmod +x /usr/local/sbin/gpdscreen

# Add script relaunch on wake
cp daemons/gpdscreen /lib/systemd/system-sleep/gpdscreen
chmod +x /lib/systemd/system-sleep/gpdscreen

# Add service to handle rotation on boot and on sleep/wake
cp daemons/gpdscreen.service /etc/systemd/system/gpdscreen.service
cp daemons/gpdscreen-wake.service /etc/systemd/system/gpdscreen-wake.service
chmod 0644 /etc/systemd/system/gpdscreen.service
chmod 0644 /etc/systemd/system/gpdscreen-wake.service

# Enable both service
systemctl enable gpdscreen.service
systemctl enable gpdscreen-wake.service

# Try to start default one
systemctl start gpdscreen.service

# Copy and install indicator for screen rotation
cp gpdscreen-indicator.py /usr/local/sbin/gpdscreen-indicator
chmod +x /usr/local/sbin/gpdscreen-indicator

# Install icons
mkdir -p /usr/local/share/gpdscreen-indicator/icons
cp icons/*.png /usr/local/share/gpdscreen-indicator/icons/
cp icons/screen-rotation-button-white.svg /usr/local/share/gpdscreen-indicator/icons/screen-rotation-button-white.svg

echo "REBOOT REQUIRED!"
