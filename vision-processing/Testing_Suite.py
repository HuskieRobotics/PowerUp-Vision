#import the necessary packages
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import serial
import time

    
#'optional' argument is required for trackbar creation parameters
def nothing(x):
    pass
 
#Capture video from the stream

cv2.namedWindow('Colorbars') #Create a window named 'Colorbars'
 
#assign strings for ease of coding
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'
#Begin Creating trackbars for each
cv2.createTrackbar(hl, wnd,0,255,nothing)
cv2.createTrackbar(hh, wnd,255,255,nothing)
cv2.createTrackbar(sl, wnd,0,255,nothing)
cv2.createTrackbar(sh, wnd,255,255,nothing)
cv2.createTrackbar(vl, wnd,0,255,nothing)
cv2.createTrackbar(vh, wnd,255,255,nothing)
cv2.createTrackbar("ISO", wnd,100,1600,nothing)
cv2.createTrackbar("Brightness", wnd,50,100,nothing)

camera = PiCamera()
camera.resolution=(320,240)
rawCapture = PiRGBArray(camera,size = (320,240))
time.sleep(.5)
##camera.exposure_mode= 'sports'
camera.brightness =5
camera.ISO = 100
#camera.sharpness = 100
#camera.contrast = 100
#camera.awb_mode = 'off'
camera.shutter_speed = 1000
print camera.shutter_speed
print camera.exposure_speed
print camera.framerate



for frame in camera.capture_continuous(rawCapture,format = 'rgb',use_video_port = True):
    
    upperHue = cv2.getTrackbarPos(hh,wnd)
    lowerHue = cv2.getTrackbarPos(hl,wnd)
    upperSat = cv2.getTrackbarPos(sh,wnd)
    lowerSat = cv2.getTrackbarPos(sl,wnd)
    upperVal = cv2.getTrackbarPos(vh,wnd)
    lowerVal = cv2.getTrackbarPos(vl,wnd)
    iso = cv2.getTrackbarPos("ISO",wnd)
    b = cv2.getTrackbarPos("Brightness",wnd)
    camera.brightness = b
    camera.ISO = iso
    lower=np.array([lowerHue,lowerSat,lowerVal],np.uint8)
    upper=np.array([upperHue,upperSat,upperVal
                    ],np.uint8)
    image = frame.array
    hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    inRange = cv2.inRange(hsv,lower,upper)

    
    cv2.imshow('inRange',inRange)
    cv2.imshow('frame',image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    rawCapture.truncate(0)


cv2.destroyAllWindows()
