import os
#from os.path import join
import glob
import cv2
import numpy as np 
import matplotlib.pyplot as plt
import time

import json, codecs

from statistics import mean
from collections import Counter
from areaOptionalFunctions import caculateArea

startTime = time.time()

errorList = []
areaList = []

areaListFilePath = '/home/tien/OpenCV/learnHandAreaThreshold/availableData/areaListFile.json'
errorListFilePath = '/home/tien/OpenCV/learnHandAreaThreshold/availableData/errorListFile.json'
pictureQuantity = 0

minArea = 0
maxArea = 0

"""
#see detail edge value???
minAreaFilePath = ''
maxAreaFilePath = ''
"""

try:
    with open(areaListFilePath, 'r+') as areaListFile:
        areaList = json.load(areaListFile)
    with open(errorListFilePath, 'r+') as errorListFile:
        errorList = json.load(errorListFile)

    print('Got AVAILABLE data')
except:
    print('Data NOT AVAILABLE. Start exploring root data:')
    myPath = "/home/tien/OpenCV/Skin/Data/SegmentedData"

    #pick all png image
    """
    for root, directories, filenames in os.walk(myPath):
        if filenames:
            
            imgPath = os.path.join(root, filenames[0])
            #print(imgPath)
            img = cv2.imread(imgPath)
            frameHeight = img.shape[0]
            frameWidth  = img.shape[1]
            break
    print('Got frameSize', frameHeight, frameWidth)
    """
    def quickQuitFunction():
        global pictureQuantity
        pictureQuantity = 0
        count = 5000
        
        for root, directories, filenames in os.walk(myPath):
            for filename in filenames:
                if filename.endswith(".png"):
                    pngImageFilePath = os.path.join(root, filename)
                    print('Working with: ', pngImageFilePath)
                    try:
                        pngImage = cv2.imread(pngImageFilePath)
                        areaList.append(caculateArea(pngImage))
                        pictureQuantity += 1
                    except:
                        errorList.append(pngImageFilePath)
                        print("Error!")
                    count = count - 1
                    if count == 0:
                        return                            
        return
    
    quickQuitFunction()

    print('Sucessful iterated', pictureQuantity, ' PNG images. Area List Updated!', len(errorList), ' errors.')                        
    #print(errorList)

    #SAVE data to FILES!
    with open(areaListFilePath, 'w') as areaListFile:
        json.dump(areaList, areaListFile)
    with open(errorListFilePath, 'w') as errorListFile:
        json.dump(errorList, errorListFile)

    print('Data saved to files')

print('Min area = ', min(areaList))
print('Mean area = ', mean(areaList))
print('Max area = ', max(areaList))

plt.title("Hand-Area Gaussian Histogram")
plt.xlabel("Area Value")
plt.ylabel("Frequency")
plt.hist(areaList)
plt.show()

print("Program executed in %s seconds " %(time.time() - startTime))
