# -*- coding: utf-8 -*-
import numpy as np 
import cv2 
import sys
from matplotlib import pyplot as plt


if __name__ == "__main__":
    if len(sys.argv)>1:
        img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print('Usage: python threshold.py imageFile')
        sys.exit(0)

    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['original image', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
