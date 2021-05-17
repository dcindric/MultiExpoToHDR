import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import skimage.io

image_path = (r"C:\Users\Korisnik\Documents\Josip\IQuiz\redskinsi.png")

def loadImage(path):
    image_file = skimage.io.imread(path, plugin = 'pil')
    return image_file

def display(a, b, title1 = "Original", title2 = "Edited"):
    plt.subplot(121), plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(b), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()
    
def resize(data):
    img=data
    print('Original size',img.shape)
    height = 220
    width = 220
    dim = (width, height)
    res_img = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
    print("RESIZED", res_img.shape)
    display(img, res_img)
    
def main():
    global image_path         
    dataset = loadImage(image_path)
    pro = resize(dataset)   
main()
