import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys
import cv2
from perspec import createPerspectiveImages
from distinguishing import coveredOrNot
from circleDetection import detectHoles, drawActualCircles

#vid = cv2.VideoCapture(3)
#vid.set(3, 1280)
#vid.set(4, 360)
#while(True):
#    ret,frame = vid.read()
#    cv2.imshow('Frame', frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'): #Use frame for analysis
#        break
#    elif cv2.waitKey(1) & 0xFF == 27: #Exit if ESC key is pressed
#        exit()
#color_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#filePath = r"img.jpg" #save last frame
#color_img.save(fp=filePath)
#mpimg.imread(filePath)
image = cv2.imread(r"img.jpg")

#RUN ANALYSIS ALGORITHM HERE, SAVE OUTPUT AS plot.jpg
topView, botView, topOnly = createPerspectiveImages(image)
cropTop = topOnly[0:540, 0:1920]

circlesCropTop, overlapsCropTop = detectHoles(cropTop, 0)
circlestopView, overlapstopView = detectHoles(topView, 1)
circlesbotView, overlapsbotView = detectHoles(botView, 2)

bigBoolCropTop = coveredOrNot(cropTop, circlesCropTop, overlapsCropTop)
bigBooltopView = coveredOrNot(topView, circlestopView, overlapstopView)
bigBoolbotView = coveredOrNot(botView, circlesbotView, overlapsbotView)

finalcropTop = drawActualCircles(cropTop,circlesCropTop,overlapsCropTop,bigBoolCropTop)
finaltopView = drawActualCircles(topView,circlestopView,overlapstopView,bigBooltopView)
finalbotView = drawActualCircles(botView,circlesbotView,overlapsbotView,bigBoolbotView)


cv2.imwrite("final1.jpg", finalcropTop)
cv2.imwrite("final2.jpg", finaltopView)
cv2.imwrite("final3.jpg", finalbotView)
cv2.imshow("Analysis Finished1",finalcropTop)
cv2.imshow("Analysis Finished2",finaltopView)
cv2.imshow("Analysis Finished3",finalbotView)
cv2.waitKey()