#!/bin/sh
set -x

sudo rpi-update
sudo apt-get -y update
sudo apt-get -y upgrade


sudo sh /home/pi/Huskie-Vision/setup/enable_cam.sh

sudo sh /home/pi/Huskie-Vision/setup/pip_installs.sh

sudo sh /home/pi/Huskie-Vision/setup/install_opencv.sh

sudo sh /home/pi/Huskie-Vision/setup/enable_systemd_service.sh

sudo shutdown -r now
