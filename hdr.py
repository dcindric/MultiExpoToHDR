import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import skimage.io
from natsort import natsorted, ns


def load_images():

    '''Load original, non-edited images. Modify image folder according to your original image directory.'''

    orig_img_files = os.listdir(r'C:\Users\Dino\Desktop\MultiExpoHDR\Originals')
    orig_img_files = natsorted(orig_img_files)
    orig_img = []

    for filename in orig_img_files:
        orig_img.append(skimage.io.imread(filename))

    for i in range(len(orig_img)):
        orig_img[i] = cv2.cvtColor(orig_img[i], cv2.COLOR_RGB2BGR)
        #orig_img[i] = cv2.cvtColor(orig_img[i], cv2.COLOR_BGR2GRAY)

    return orig_img



def allign_images(img):

    '''Image allignment is needed because even a small vibrations of camera can cause image distortion.
    This function converts input images to median treshold bitmaps (MTB), which is invariant to camera
    exposure time.'''

    img_alligned = []

    MTB_img = cv2.createAlignMTB()


orig_img = load_images()


plt.imshow(orig_img[2])
plt.show()




