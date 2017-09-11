#!/bin/bash

cp gpdscreen-indicator.py /usr/local/sbin/gpdscreen-indicator
chmod +x /usr/local/sbin/gpdscreen-indicator

cp gpdscreen-indicator.service /etc/systemd/system/gpdscreen-indicator.service

chmod 0644 /etc/systemd/system/gpdscreen-indicator.service

systemctl enable gpdscreen-indicator.service

mkdir -p /usr/local/share/gpdscreen-indicator/icons
cp icons/* /usr/local/share/gpdscreen-indicator/icons/
