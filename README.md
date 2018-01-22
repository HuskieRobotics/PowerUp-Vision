# Huskie-Vision
Our teams template for future vision projects. Contains a variety of setup scripts that should be run to enable the camera and import OpenCV libraries. Also has a template for processing images via the Pi Camera and creating a UDP server. 


## Stuff to buy 

1. Buy a Raspberry Pi and Pi Camera v2 from [here](https://www.raspberrypi.org/products/)

2. Buy a case [here](https://www.amazon.com/Raspberry-Model-Protective-Heatsinks-Clear/dp/B01CDVSBPO/ref=sr_1_4?s=electronics&ie=UTF8&qid=1501820103&sr=1-4&keywords=raspberry+pi+case)

3. Buy a [camera case](https://www.amazon.com/Latest-Raspberry-Camera-Case-Megapixel/dp/B00IJZJKK4/ref=sr_1_2?s=electronics&ie=UTF8&qid=1501820315&sr=1-2&keywords=camera+case+raspberry+pi)

4. You'll also need a mini sd card (8GB +), you can buy this anywhere

5. Buy a [LED RING](http://www.andymark.com/product-p/am-3596.htm)

## Setup

1. Download Raspbian onto your personal computer: [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) 

2. Download [Etcher](https://etcher.io/) and flash the pi using the Raspbian image.

3. Once your SD card is formatted, place an empty text file called ssh in the boot folder to enable SSH. You can then install [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) on your desktop to access the pi. Then hook up your pi to your internet (via ethernet cable) and then ssh into the pi using putty with a hostname of ```raspberrypi.local``` a username of ```pi``` and a password of ```raspberry```. You may change these once in the terminal by running ```sudo raspi-config```. This is the easiest way to access the shell of the RPI however you may also hook up a monitor, keyboard, and mouse if you would like to use the desktop.

4. Make sure your pi is connected to the internet and install git via ```sudo apt-get install git``` or follow these [instructions](https://www.raspberrypi.org/learning/getting-started-with-git/worksheet/)

5. Then fork this [repository](https://github.com/HuskieRobotics/Huskie-RPi-Vision-Public) and clone it. Instructions [here](https://guides.github.com/activities/forking/)... If you do not have access to the desktop/web browser you may just clone the repository.
To just clone use ```git clone https://github.com/HuskieRobotics/Huskie-Vision```

6. Now run my setup file (it may take up to 6 hours+ to compile the opencv library, run this overnight). Use the commands
```
sudo chmod +x /home/pi/Huskie-Vision/setup/setup_script.sh
sudo sh /home/pi/Huskie-Vision/setup/setup_script.sh
```


## Programming Vision
1. Take a look at the vision files and fill in your code as necessary. There are a variety of comments that detail exactly how and where to write your code. 

2. Also make sure to use the Testing Suite to tune your camera using HSV, Brightness, ISO, etc. It contains trackbars that you can slide around to tune. 

## What do the files do???
1. ```/setup/setup_script.sh```  This file runs all the setup scripts

2. ```/setup/VisionStartup.service``` This file is a systemd service. It is copied into the file path ```etc/systemd/system/``` and given permissions that allow it run the Vision Processing when the Pi boots up. Basically autoruns the program on startup so you don't have to during competition.

3. ```/setup/enable_systemd_service.sh``` This file sets up the ```VisionStartup.service``` file in the systemd service folder.

4. ```/setup/enable_cam.sh``` This file enables the camera module. You don't necessarily need this if you use a USB camera.

5. ```/setup/install_opencv.sh``` This file installs OpenCV for Python 2.7. It does take a long time to run.

6. ```/setup/launcher.sh``` This file launches the Vision Processing. Is called by the systemd service.

7. ```/setup/pip_installs.sh``` This file uses pip to install all other relevant modules including numpy, socket, and time.

8. ```/vision processing/Image_Processing.py``` This file takes the image, finds the contours, and gets all the data you would like from the image.

9. ```/vision processing/Testing Suite.py``` This file is a testing suite for your HSV, brightness, and ISO tuning.You will then use these values and plug them into your image processing thresholding.

10. ```/vision processing/UDP_Server.py``` Class for the UDP server object that sends JSON packets to the roborio. 

11. ```/vision processing/Vision_Main.py``` Main Vision program where images are grabbed from camera and the server and Image Processing modules are called.

## Important Links

Team 254 Vision Video SUPER HELPFUL: [here](https://www.team254.com/documents/vision-control/)

Vision Tracking in FRC (A short guide): [here](https://medium.com/@christopherariagno/vision-tracking-in-frc-what-ive-learned-this-year-2bbb2e713794)

Learning about OpenCV: [here](http://docs.opencv.org/3.1.0/d2/d96/tutorial_py_table_of_contents_imgproc.html)

Learning about Contours: [here](http://docs.opencv.org/3.1.0/d3/d05/tutorial_py_table_of_contents_contours.html)

What is UDP: [here](http://searchmicroservices.techtarget.com/definition/UDP-User-Datagram-Protocol)

## 3D Printed Camera Cases

Our GrabCad Partner space has the files for all of this: [here](https://workbench.grabcad.com/workbench/projects/gcGE8V6qjJTC8MVGvCVHrsE53Zv-qneaUuiebfHzCsZ08G#/space/gcYgMNwN-ZOnUh87_eJl-JzqzF4mV5uck80jfpLCJ3wMqS)  This model actually has a spot for the LED ring to sit on. 
