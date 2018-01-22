##This file processes the stream of images
import cv2
import time
import numpy as np


###Set these to your preferred ranges for HSV based on the data you collected from the Testing Suite
lowerC = np.array([40,75, 25])
upperC = np.array([70, 255, 190])

def process_image(image):
    #Initialize all the data you are going to collect to 0. This ensures that if the target is not detected, it will return 0 and not an error
    #ex. targetX,targetY,Area = 0,0,0
    targetX, targetY, targetH, targetW = 0,0,0,0
    #using hsv to threshold is recommended, the inRange function basically cuts out all colors that arent wanted
    hsvFrame = cv2.cvtColor(image, COLOR_RGV2HSV)
    thresholdedFrame = cv2.inRange(newFrame, lowerC, upperC)

    try:
         targetX, targetY, targetW, targetH = calculations(thresholdedFrame)
        ###operations on the frame come here, set all the variables to desired numbers based on contours and other things you find from the image
        ###ex. targetX = getX(thresholdedFrame)
    except:
        pass

    ###Here return the data you have collected
    ###ex return targetX,targetY,Area
    return (targetX, targetY, targetH, targetW)

def calculations(frame):
    rectangles = detectRectangles(image)
    leftRectangle, rightRectangle = rectangleStats(rectangles)
    targetX,targetY = getCenter(leftRectangle,rightRectangle)
    targetW = rightRectangle[0] - leftRectangle[0] +leftRectangle[2]
    targetH =(rightRectangle[3]+leftRectangle[3])/2.0
    return (targetX, targetY, targetW, targetH)

def detectRectangles(image):
    a,contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    rectangles = findRectangles(contours)
    rectangles = sorted(rectangles, key = cv2.contourArea,reverse=True)[:10]

    index = len(rectangles)-1
    while index>=0:
        x,y,w,h = cv2.boundingRect(rectangles[index])
        area= cv2.contourArea(rectangles[index])
        #checks for correct aspect ratio of the rectangles
        if ((abs(float(w)/h - 7.5)>.7) and (abs(float(h)/w- 7.5) >.7)):
            rectangles.pop(index)

        #checks if area is within reasonable range
        elif area< 500 or area>15000:
            rectangles.pop(index)
        index-=1

    return rectangles
def findRectangles(contours):
    returnList = []
    for r in contours:
        returnList.append(np.int0(cv2.boxPoints(cv2.minAreaRect(r))))
    return returnList

def rectangleStats(rectangles):
    x,y,w,h = cv2.boundingRect(rectangles[0])
    x2,y2,w2,h2 = cv2.boundingRect(rectangles[1])
    if x<x2:
        leftRectangle = [x,y,w,h]
        rightRectangle = [x2,y2,w2,h2]
    else:
        leftRectangle = [x2,y2,w2,h2]
        rightRectangle = [x,y,w,h]
    return leftRectangle,rightRectangle


def getCenter(leftRectangle,rightRectangle):
    #x + w + x2 / 2.0 middle of two x coordinates
    centerX = float(leftRectangle[0]+leftRectangle[2]+rightRectangle[0])/2.0
    #2(y)+h +2(y2)+h2 / 4.0  average of the two height centers
    centerY = float((2*leftRectangle[1])+leftRectangle[3]+(2*rightRectangle[1])+rightRectangle[3])/4.0
    return centerX,centerY
###SET THE REST OF YOUR FUNCTIONS AND OPERATIONS ON THE FRAME HERE

#things to try
#Finding contours : foo, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Finding rectangles around contour : rectangle = np.int0(cv2.boxPoints(cv2.minAreaRect(contour)))
#Finding area of contour : area = cv2.contourArea(contour)


#USE THE INTERNET AND VAST AMOUNTS OF INFORMATION TO FIGURE OUT WHICH CV2 FUNCTIONS
#YOU NEED TO USE IN ORDER TO GET THE DATA YOU WANT, OUR GITHUB HAS MANY USEFUL LINKS
