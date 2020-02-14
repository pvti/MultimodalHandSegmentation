import cv2
import numpy as np 
import matplotlib.pyplot as plt

#learn the width & height thresh
def caculateWidthAndHeight(pngImage):
    pngImageGray = cv2.cvtColor(pngImage, cv2.COLOR_BGR2GRAY)
    __, contours, __ = cv2.findContours(pngImageGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    

    #draw straight bounding rectangle
    x, y, width, height = cv2.boundingRect(contours[0])
    #cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255),2)
    return {'width':width, 'height':height}
