#!/bin/sh

set -x

cd ~


sudo apt-get autoremove -y
sudo apt-get autoremove -y opencv-doc \ 
	opencv-data \
	libopencv-dev \
	libopencv2.4-java \
	libopencv2.4-jni \
	python-opencv \
	libopencv-core2.4 \
	libopencv-gpu2.4 \
	libopencv-ts2.4 \
	libopencv-photo2.4 \
	libopencv-contrib2.4 \
	libopencv-imgproc2.4 \
	libopencv-superres2.4 \
	libopencv-stitching2.4 \
	libopencv-ocl2.4 \
	libopencv-legacy2.4 \
	libopencv-ml2.4 \
	libopencv-video2.4 \
	libopencv-videostab2.4 \
	libopencv-objdetect2.4 \
	libopencv-calib3d2.4
sudo apt-get purge libopencv* -y
sudo dpkg -r opencv

sudo apt-get install -y build-essential cmake cmake-curses-gui pkg-config -y
sudo apt-get install libatlas-base-dev gfortran -y
sudo apt-get install -y \
	libpango1.0-dev \
	libgdk-pixbuf2.0-dev \
	libcairo2-dev \
	libjpeg-dev \
	libtiff5-dev \
	libjasper-dev \
    	libpng12-dev \
    	libavcodec-dev \
    	libavformat-dev \
    	libswscale-dev \
    	libeigen3-dev \
    	libxvidcore-dev \
    	libx264-dev \
    	libgtk2.0-dev \


sudo apt-get install python2.7-dev python3-dev -y
sudo pip install numpy
sudo pip3 install numpy


mkdir /home/pi/opencv && cd /home/pi/opencv
wget https://github.com/opencv/opencv/archive/3.2.0.zip -O opencv_source.zip
wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip -O opencv_contrib.zip
unzip opencv_source.zip
unzip opencv_contrib.zip
cd /home/pi/opencv/opencv-3.2.0 && mkdir build && cd build

sudo cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D BUILD_WITH_DEBUG_INFO=OFF \
    -D BUILD_DOCS=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_opencv_ts=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules \
    -D ENABLE_NEON=ON \
    -D WITH_LIBV4L=ON \
        ../

sudo make
sudo make install
sudo ldconfig
