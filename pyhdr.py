import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import skimage.io
from natsort import natsorted, ns


def load_images():

    '''Load original, non-edited images. Modify image folder according to your original image directory.'''

    #Change directory!!! 
    orig_img_files = os.listdir(r'C:\Users\Dino\Desktop\MultiExpoHDR\Originals')
    orig_img_files = natsorted(orig_img_files)
    orig_img = []

    for filename in orig_img_files:
        orig_img.append(skimage.io.imread(filename))

    for i in range(len(orig_img)):
        orig_img[i] = cv2.cvtColor(orig_img[i], cv2.COLOR_RGB2BGR)
        #orig_img[i] = cv2.cvtColor(orig_img[i], cv2.COLOR_BGR2GRAY)

    return orig_img


def align_images(img):

    '''Image alignment is needed because even a small vibrations of camera can cause image distortion.
    This function converts input images to median treshold bitmaps (MTB), which is invariant to camera
    exposure time.'''

    img_alligned = []
    allignMTB = cv2.createAlignMTB()
    allignMTB.process(img, img_alligned)

    alignMTB = cv2.createAlignMTB()
    alignMTB.process(img, img)

    img_alligned = img

    return img_alligned




def merge_images_mertens(img):
    
    '''Merging previously aligned images into one image.'''


    if(merge_type == 'mertens'):

        mertens_merge = cv2.createMergeMertens()
        img_merged = mertens_merge.process(img)

    else:
        print('Wrong input argument!')

    return img_merged



def merge_images_debevec(img, exposure_times):
    
    #For Debevec algorithm, we need to know exposure times! If images are annotated, this can be extracted from image metadata. 
    # Tone mapping is also required for Debevec function.   
    if(merge_type == 'debevec'):

        debevec_merge = cv2.createMergeDebevec()
        img_merged = debevec_merge.process(img, times = exposure_times.copy())
        tonemap_debevec = cv2.createTonemap(gamma = 2.0)
        res_debevec = tonemap1.process(img_merged.copy())
        img_merged = res_debevec

    else:
        print('Wrong input argument!')

    return img_merged



def merge_images_robertson(img, exposure_times):

    if(merge_type == 'robertson'):

        robertson_merge = cv2.createMergeRobertson()
        img_merged = robertson_merge.process(img, times = exposure_times.copy())

        tonemap_robertson = cv2.createTonemap(gamma = 2.0)

        res_robertson = tonemap1.process(img_merged.copy())
        img_merged = res_robertson

    else:
        print('Wrong input argument!')

    return img_merged




def convert_and_save(img):

    '''Converts image into [0, 255] 8-bit range.'''

    img_cnvt = np.clip(img * 255, 0, 255).astype('uint8')
    cv2.imwrite("HDR", img_cnvt)



