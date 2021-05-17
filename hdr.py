#Custom submodule
from pyhdr import *

#Example

#First, load original images with different exposure times.
orig_img = load_images()


#Because even a small vibration of camera can cause image distortion and possible misalignment of images with different exposure, 
#image aligning needs to be performed.
aligned_img = align_images(orig_img)



#Merge images with Mertens algorithm - exposure times are NOT needed for this algorithm. 
hdr_img_mertens = merge_images_mertens(aligned_img, 'mertens')



#Show acquired HDR image (Mertens)
""" plt.imshow(hdr_img_mertens)
plt.show()

plt.imshow(hdr_img_debevec_NO_CRF)
plt.show()

plt.imshow(hdr_img_debevec_CRF)
plt.show()

plt.imshow(hdr_img_robertson_NO_CRF)
plt.show()

plt.imshow(hdr_img_robertson_CRF)
plt.show() """




#convert_and_save(hdr_img)