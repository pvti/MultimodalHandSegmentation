import os
#from os.path import join
import glob
import cv2
import numpy as np 
import matplotlib.pyplot as plt
import time

from sklearn import preprocessing
import json, codecs

startTime = time.time()

"""
rSkinAmount = np.zeros((256,), dtype=int)
gSkinAmount = np.zeros((256,), dtype=int)
bSkinAmount = np.zeros((256,), dtype=int)
"""
hSkinAmount = np.zeros((180,), dtype=int)
sSkinAmount = np.zeros((256,), dtype=int)
vSkinAmount = np.zeros((256,), dtype=int)

#print(rSkinAmount[255])

"""
rNotSkinAmount = np.zeros((256,), dtype=int)
gNotSkinAmount = np.zeros((256,), dtype=int)
bNotSkinAmount = np.zeros((256,), dtype=int)
"""
hNotSkinAmount = np.zeros((180,), dtype=int)
sNotSkinAmount = np.zeros((256,), dtype=int)
vNotSkinAmount = np.zeros((256,), dtype=int)


errorList = []

"""
rSkinAmountFile = '/home/tien/OpenCV/skinStatistic/groundTruthData/rSkinAmount.json'
gSkinAmountFile = '/home/tien/OpenCV/skinStatistic/groundTruthData/gSkinAmount.json'
bSkinAmountFile = '/home/tien/OpenCV/skinStatistic/groundTruthData/bSkinAmount.json'

rNotSkinAmountFile = '/home/tien/OpenCV/skinStatistic/groundTruthData/rNotSkinAmount.json'
gNotSkinAmountFile = '/home/tien/OpenCV/skinStatistic/groundTruthData/gNotSkinAmount.json'
bNotSkinAmountFile = '/home/tien/OpenCV/skinStatistic/groundTruthData/bNotSkinAmount.json'
"""
hSkinAmountFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/hSkinAmount.json'
sSkinAmountFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/sSkinAmount.json'
vSkinAmountFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/vSkinAmount.json'

hNotSkinAmountFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/hNotSkinAmount.json'
sNotSkinAmountFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/sNotSkinAmount.json'
vNotSkinAmountFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/vNotSkinAmount.json'



errorListFile = '/home/tien/OpenCV/learnHSVthreshold/groundTruthData/errorListFile.json'

try:
    hSkinAmountText = codecs.open(hSkinAmountFile, 'r', encoding='utf-8').read()
    toListHSkinAmount = json.loads(hSkinAmountText)
    hSkinAmount = np.array(toListHSkinAmount)
    
    sSkinAmountText = codecs.open(sSkinAmountFile, 'r', encoding='utf-8').read()
    toListSSkinAmount = json.loads(sSkinAmountText)
    sSkinAmount = np.array(toListSSkinAmount)

    vSkinAmountText = codecs.open(vSkinAmountFile, 'r', encoding='utf-8').read()
    toListVSkinAmount = json.loads(vSkinAmountText)
    vSkinAmount = np.array(toListVSkinAmount)

    hNotSkinAmountText = codecs.open(hNotSkinAmountFile, 'r', encoding='utf-8').read()
    toListHNotSkinAmount = json.loads(hNotSkinAmountText)
    hNotSkinAmount = np.array(toListHNotSkinAmount)
    
    sNotSkinAmountText = codecs.open(sNotSkinAmountFile, 'r', encoding='utf-8').read()
    toListSNotSkinAmount = json.loads(sNotSkinAmountText)
    sNotSkinAmount = np.array(toListSNotSkinAmount)

    vNotSkinAmountText = codecs.open(vNotSkinAmountFile, 'r', encoding='utf-8').read()
    toListVNotSkinAmount = json.loads(vNotSkinAmountText)
    vNotSkinAmount = np.array(toListVNotSkinAmount)

    with open(errorListFile, 'r+') as errorListF:
        errorList = json.load(errorListF)

    print('Got AVAILABLE data')
except:
    print('Data NOT AVAILABLE. Start exploring root data:')
    def hSVAmountUpdateByComparing2Images(pngImage, jpgImage, frameHeight, frameWidth):
        #pngImage = pngImage[..., ::-1]
        jpgHSVImage = cv2.cvtColor(jpgImage, cv2.COLOR_BGR2HSV)

        for i in range(frameHeight):
            for j in range(frameWidth):
                h = jpgHSVImage.item(i, j, 0)
                s = jpgHSVImage.item(i, j, 1)
                v = jpgHSVImage.item(i, j, 2)
                if pngImage.item(i, j, 0) == 255:
                    hSkinAmount[h] += 1
                    sSkinAmount[s] += 1
                    vSkinAmount[v] += 1
                else:
                    hNotSkinAmount[h] += 1
                    sNotSkinAmount[s] += 1
                    vNotSkinAmount[v] += 1
        return 0

    myPath = "/home/tien/OpenCV/Skin/Data/SegmentedData"

    #print(myPath)

    #pick an typical random image to get image's frame size; 1 time only for all others
    for root, directories, filenames in os.walk(myPath):
        if filenames:
            
            imgPath = os.path.join(root, filenames[0])
            #print(imgPath)
            img = cv2.imread(imgPath)
            frameHeight = img.shape[0]
            frameWidth  = img.shape[1]
            break
    print('Got frameSize', frameHeight, frameWidth)

    #start matching png vs jpg
    #myPath as level0Files
    # def myFunc(): #using myFunc to quit multi loops
    level1Files = os.listdir(myPath)  #level1Files = ['Binh', 'Hung', 'Hoang']
    # print(level1Files)
    for level1File in level1Files: 
        level1FilesPath = os.path.join(myPath, level1File)
        # print (level1FilesPath) # level1FilesPath = /home/tien/OpenCV/Skin/Data/SegmentedData/Binh
        level2Files = os.listdir(level1FilesPath) 
        for level2File in level2Files:
            level2FilesPath = os.path.join(level1FilesPath, level2File)
            # print(level2FilesPath) # level2FilesPath = /home/tien/OpenCV/Skin/Data/SegmentedData/Binh/1
            level3Files = os.listdir(level2FilesPath)
            # print(level3Files) # level3Files = ['5 (3-19-2018 10-18-43 AM)', '1 (3-19-2018 10-18-37 AM)', '4.1', '3 (3-19-2018 10-18-39 AM)', '2 (3-19-2018 10-18-38 AM)', '1.1', '2.1', '5.1', '3.1', '4 (3-19-2018 10-18-41 AM)']
            
            for level3FileLabel in level3Files: # level3FileLabel = ['1.1']
                if len(level3FileLabel) > 4:
                    continue
                for level3FileOrigin in level3Files: # level3FileOrigin = ['1 (3-19-2018 10-18-37 AM)']
                    if len(level3FileOrigin) > 4 and level3FileLabel.split('.')[0] == level3FileOrigin.split(' ')[0] :
                        pngFinalPath = os.path.join(level2FilesPath, level3FileLabel)
                        jpgFinalPath = os.path.join(level2FilesPath, level3FileOrigin)
                        # print(pngFinalPath, " ", jpgFinalPath)
                        pngImages = os.listdir(pngFinalPath)
                        jpgImages = os.listdir(jpgFinalPath)
                        for jpgImage in jpgImages:
                            matchedIndex = jpgImage.split('.')[0]+'.png' # matchedIndex = 3 11.pgn
                            #print(matchedIndex)
                            pathJPG = os.path.join(jpgFinalPath, jpgImage)
                            pathPNG = os.path.join(pngFinalPath, matchedIndex)
                            print("Working with: ", pathJPG, " and ", pathPNG)
                            
                            try:
                                imageFromPathPNG = cv2.imread(pathPNG)
                                imageFromPathJPG = cv2.imread(pathJPG)                        
                                hSVAmountUpdateByComparing2Images(imageFromPathPNG, imageFromPathJPG, frameHeight, frameWidth)                                    
                            except:
                                errorList.append(pathJPG)
                                print("Error!")
    print('Sucessful Compared all matchable pairs PNG-JPG. Amount Updated! ErrorList (segmented errors) below: ')                        
    print(errorList)

    #SAVE data to FILES!
    toListHSkinAmount = hSkinAmount.tolist()
    toListSSkinAmount = sSkinAmount.tolist()
    toListVSkinAmount = vSkinAmount.tolist()
    
    toListHNotSkinAmount = hNotSkinAmount.tolist()
    toListSNotSkinAmount = sNotSkinAmount.tolist()
    toListVNotSkinAmount = vNotSkinAmount.tolist()
    
    #below line save data in .json format JSONIFY 
    json.dump(toListHSkinAmount, codecs.open(hSkinAmountFile, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    json.dump(toListSSkinAmount, codecs.open(sSkinAmountFile, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    json.dump(toListVSkinAmount, codecs.open(vSkinAmountFile, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    json.dump(toListHNotSkinAmount, codecs.open(hNotSkinAmountFile, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    json.dump(toListSNotSkinAmount, codecs.open(sNotSkinAmountFile, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    json.dump(toListVNotSkinAmount, codecs.open(vNotSkinAmountFile, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

    with open(errorListFile, 'w') as errorListF:
        json.dump(errorList, errorListF)

    print('Data saved to files')
# try to standardlize the data manually
maxValueOfHSkinAmount = max(hSkinAmount)
maxValueOfSSkinAmount = max(sSkinAmount)
maxValueOfVSkinAmount = max(vSkinAmount)

standardlizedHSkinAmount = np.zeros((256,))
standardlizedSSkinAmount = np.zeros((256,))
standardlizedVSkinAmount = np.zeros((256,))

for i in range(180):
    standardlizedHSkinAmount[i] = hSkinAmount[i] / maxValueOfHSkinAmount

for i in range(256):
    standardlizedSSkinAmount[i] = sSkinAmount[i] / maxValueOfSSkinAmount
    standardlizedVSkinAmount[i] = vSkinAmount[i] / maxValueOfVSkinAmount

maxValueOfHNotSkinAmount = max(hNotSkinAmount)
maxValueOfSNotSkinAmount = max(sNotSkinAmount)
maxValueOfVNotSkinAmount = max(vNotSkinAmount)

standardlizedHNotSkinAmount = np.zeros((180,))
standardlizedSNotSkinAmount = np.zeros((256,))
standardlizedVNotSkinAmount = np.zeros((256,))

for i in range(180):
    standardlizedHNotSkinAmount[i] = hNotSkinAmount[i] / maxValueOfHNotSkinAmount


for i in range(256):
    standardlizedSNotSkinAmount[i] = sNotSkinAmount[i] / maxValueOfSNotSkinAmount
    standardlizedVNotSkinAmount[i] = vNotSkinAmount[i] / maxValueOfVNotSkinAmount

#process data, optional!

fixHNotSkinAmount = hNotSkinAmount
fixSNotSkinAmount = sNotSkinAmount
fixVNotSkinAmount = vNotSkinAmount

fixHNotSkinAmount[179] = fixHNotSkinAmount[179]
fixSNotSkinAmount[255] = fixSNotSkinAmount[254]
fixVNotSkinAmount[255] = fixVNotSkinAmount[254]

maxValueOfFixHNotSkinAmount = max(fixHNotSkinAmount)
maxValueOfFixSNotSkinAmount = max(fixSNotSkinAmount)
maxValueOfFixVNotSkinAmount = max(fixVNotSkinAmount)

standardlizedFixHNotSkinAmount = np.zeros((180,))
standardlizedFixSNotSkinAmount = np.zeros((256,))
standardlizedFixVNotSkinAmount = np.zeros((256,))

for i in range(180):
    standardlizedFixHNotSkinAmount[i] = fixHNotSkinAmount[i] / maxValueOfFixHNotSkinAmount


for i in range(256):
    standardlizedFixSNotSkinAmount[i] = fixSNotSkinAmount[i] / maxValueOfFixSNotSkinAmount
    standardlizedFixVNotSkinAmount[i] = fixVNotSkinAmount[i] / maxValueOfFixVNotSkinAmount

"""
#using preprocessing library #NOT UNDERSTOOD!
reshapedRSkinAmount = rSkinAmount.reshape(-1, 1)
normalizedRSkinAmount = preprocessing.normalize(reshapedRSkinAmount)
print (normalizedRSkinAmount)
"""

#hue skin plot
plt.subplot(431)
plt.title('Hue Amount Plot')
# plt.xlabel('Pixel Value')
plt.ylabel('Amount')
plt.plot (hSkinAmount, 'r')

#saturation skin plot
plt.subplot(432)
plt.title('Saturation Amount Plot')
# plt.xlabel('Pixel Value')
plt.ylabel('Amount')
plt.plot (sSkinAmount, 'g')

#value skin plot
plt.subplot(433)
plt.title('Value Amount Plot')
# plt.xlabel('Pixel Value')
plt.ylabel('Amount')
plt.plot (vSkinAmount, 'b')

#hue vs non-hue skin plot
plt.subplot(434)
plt.title('Hue vs Non-Hue Amount Plot')
# plt.xlabel('Pixel Value')
plt.ylabel('Amount')
plt.plot(hSkinAmount, 'r', hNotSkinAmount, 'k')
#plt.show()

#Saturation vs Saturation-value skin plot
plt.subplot(435)
plt.title('Saturation vs Non-Saturation Amount Plot')
# plt.xlabel('Pixel Value')
plt.ylabel('Amount')
plt.plot(sSkinAmount, 'g', sNotSkinAmount, 'k')
#plt.show()

#Value vs non-value skin plot
plt.subplot(436)
plt.title('Value vs Non-Value Amount Plot')
# plt.xlabel('Pixel Value')
plt.ylabel('Amount')
plt.plot(vSkinAmount, 'b', vNotSkinAmount, 'k')

#Standardlized Amount plot

#standardlized: hue vs non-hue skin plot
plt.subplot(437)
plt.title('Standardlized hue vs non-hue')
plt.plot(standardlizedHSkinAmount, 'r', standardlizedHNotSkinAmount, 'k')

#standardlized: saturation vs non-saturation skin plot
plt.subplot(438)
plt.title('Standardlized saturation vs non-saturation')
plt.plot(standardlizedSSkinAmount, 'g', standardlizedSNotSkinAmount, 'k')

#standardlized: value vs non-value skin plot
plt.subplot(439)
plt.title('Standardlized value vs non-value')
plt.plot(standardlizedVSkinAmount, 'b', standardlizedVNotSkinAmount, 'k')

#standardlized fixed: hue vs non-hue skin plot
plt.subplot(4, 3, 10)
plt.title('Fixed Standardlized hue vs non-hue')
plt.plot(standardlizedHSkinAmount, 'r', standardlizedFixHNotSkinAmount, 'k')

#standardlized fixed: saturation vs non-saturation skin plot
plt.subplot(4, 3, 11)
plt.title('Fixed Standardlized saturation vs non-saturation')
plt.plot(standardlizedSSkinAmount, 'g', standardlizedFixSNotSkinAmount, 'k')

#standardlized fixed: value vs non-value skin plot
plt.subplot(4, 3, 12)
plt.title('Fixed Standardlized value vs non-value')
plt.plot(standardlizedVSkinAmount, 'b', standardlizedFixVNotSkinAmount, 'k')

print("Program executed in %s seconds " %(time.time() - startTime))

plt.show()

#myFunc