import cv2
import numpy as np 
import matplotlib.pyplot as plt
"""
originalImage=cv2.imread('/home/tien/OpenCV/Skin/Data/SegmentedData/Binh/1/1.1/1 01.png')
image = originalImage
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im2, contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(contours)

for contour in contours:
    area = cv2.contourArea(contour)
    print(area)
    #cv2.drawContours(image, [contour], 0, (255, 0, 255), 3)
cv2.imshow('Original Image', originalImage)
cv2.imshow('Contours Drawed Image', image)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#learn the HSV & HandArea threshold
def caculateArea(pngImage):
    pngImageGray = cv2.cvtColor(pngImage, cv2.COLOR_BGR2GRAY)
    im2, contours, hierarchy = cv2.findContours(pngImageGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    area = cv2.contourArea(contours[0])
    return area

'''
#learn the width & height thresh
def caculateWidthAndHeight(pngImage):
    pngImageGray = cv2.cvtColor(pngImage, cv2.COLOR_BGR2GRAY)
    __, contours, __ = cv2.findContours(pngImageGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    

    #draw straight bounding rectangle
    x, y, width, height = cv2.boundingRect(contours[0])
    #cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255),2)
    return (width, height)
'''