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
from WHOptionalFunctions import caculateWidthAndHeight

startTime = time.time()

errorList = []
widthList = []
heightList = []

widthListFilePath = '/home/tien/OpenCV/learnWHThreshold/availableData/widthListFile.json'
heightListFilePath = '/home/tien/OpenCV/learnWHThreshold/availableData/heightListFile.json' 

errorListFilePath = '/home/tien/OpenCV/learnWHThreshold/availableData/errorListFile.json'
pictureQuantity = 0

minWidth = 0
maxWidth = 0

minHeight = 0
maxHeight = 0

"""
#see detail edge value???
minAreaFilePath = ''
maxAreaFilePath = ''
"""

try:
    with open(widthListFilePath, 'r+') as widthListFile:
        widthList = json.load(widthListFile)
    with open(heightListFilePath, 'r+') as heightListFile:
        heightList = json.load(heightListFile)        
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
                        widthList.append(caculateWidthAndHeight(pngImage)['width'])
                        heightList.append(caculateWidthAndHeight(pngImage)['height'])
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
    with open(widthListFilePath, 'w') as widthListFile:
        json.dump(widthList, widthListFile)
    with open(heightListFilePath, 'w') as heightListFile:
        json.dump(heightList, heightListFile)
    
    with open(errorListFilePath, 'w') as errorListFile:
        json.dump(errorList, errorListFile)

    print('Data saved to files')

print('Min width = ', min(widthList))
print('Mean width = ', mean(widthList))
print('Max width = ', max(widthList))

print('Min height = ', min(heightList))
print('Mean height = ', mean(heightList))
print('Max height = ', max(heightList))

plt.subplot(121)
plt.title("Width Gaussian Histogram")
plt.xlabel("Width Value")
plt.ylabel("Frequency")
plt.hist(widthList)

plt.subplot(122)
plt.title("Height Gaussian Histogram")
plt.xlabel("Height Value")
plt.ylabel("Frequency")
plt.hist(heightList)

plt.show()

print("Program executed in %s seconds " %(time.time() - startTime))
