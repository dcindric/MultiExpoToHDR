#Custom submodule
from pyhdr import *

    

#Example

orig_img = load_images()
aligned_img = align_images(orig_img)

hdr_img = merge_images(aligned_img, 'mertens')

plt.imshow(hdr_img)
plt.show()

convert_and_save(hdr_img)