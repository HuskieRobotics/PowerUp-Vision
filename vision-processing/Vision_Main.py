#General Modules
import cv2
import time
import numpy as np
import socket

#PI Camera specific modules
from picamera.array import PiRGBArray
from picamera import PiCamera

#User created modules
import UDP_Client
from Image_Processing import process_image
import MLPredictor


def getVideo():

    #Initialize Camera Stream
    camera = PiCamera()
    camera.resolution=(320,240)

    #These values are subject to change, use the Testing Suite to determine what range of values you want
    camera.brightness =50
    camera.ISO = 100

    camera.shutter_speed = 1000
    rawCapture = PiRGBArray(camera,size=(320,240))

    ###Edit the line below and change the IP address to your robot's ip (i.e. "10.30.61.17"), port is an arbitrary number
    client = UDP_Client.Client("Robot IP",9000) #(IP,PORT)
    predictor = MLPredictor.Predictor('neuralNetGL3')

    #frame_time is a pretty precise way of getting the timestamp of your image if you need it
    frame_time = time.time()
    circular_angle_array = []
    weights = [.6,.2,.1,.05,.025,.02265,.00125,.000625,.0003125,.00015625]
    MAX_SIZE = 10
    arrayPos = 0
    for frame in camera.capture_continuous(rawCapture,format = 'bgr',use_video_port = True):
        image = frame.array

        ###DO YOUR PROCESSING HERE USING OpenCV and the image variable
        ###Refer to the Image Processing module and call its function process_image here
        targetX, targetY, targetW, targetH = process_image(image)
        coord3D = predictor.predict3D([targetX,targetY,targetW,targetH])
        angle = predictor.getAngle(coord3D)
        circular_angle_array.insert(arrayPos, angle)

        final_angles = 0
        for i in range(MAX_SIZE):
            final_angles += weights[(i)%MAX_SIZE] * circular_angle_array[(i+arrayPos)%MAX_SIZE]

        print(final_angles)
        arrayPos = (arrayPos+=1)%10

        ###Input your data and tags into the list below to send data to the rio
        ###This data is converted to a json string FYI, makes the sending faster
        client.sendData({"Angle":final_angles,"Time":frame_time})

        #this trunctates the stream of images to grab the current image
        rawCapture.truncate(0)
        frame_time = time.time()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


getVideo()
