import cv2
import numpy as np

#def loadImages():

#    imageNames = ["","",""]
#    images = []
#    for image in imageNames:
#      img = cv2.imread(image)
#      images.append(img)

#    return images

def alignImages():
    
    align = cv2.createAlignMTB()
    align.process(images, images)
    
    return images
