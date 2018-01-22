#!/bin/sh

set -x
sudo sed -i 's/start_x=0/start_x=1/g' /boot/config.txt

sudo sed -i 's/gpu_mem=128/gpu_mem=256/g' /boot/config.txt

sudo grep -q 'start_x=1' /boot/config.txt || sudo echo 'start_x=1' >> /boot/config.txt

sudo grep -q 'gpu_mem=256' /boot/config.txt || sudo echo 'gpu_mem=256' >> /boot/config.txt


