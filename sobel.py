import math
import cv2
import numpy as np
import sys
from scipy import signal


def pascalSmooth(n):
    pascalSmooth = np.zeros([1,n],np.float32)
    for i in range(n):
        pascalSmooth[0][i] = math.factorial(n-1)/(math.factorial(i)*math.factorial(n-1-i))
    return pascalSmooth


def pascalDiff(n):
    pascalDiff = np.zeros([1,n], np.float32)
    pascalSmooth_previous = pascalSmooth(n-1)
    for i in range(n):
        if i==0:
            pascalDiff[0][i] = pascalSmooth_previous[0][i]
        elif i == n-1:
            pascalDiff[0][i] = -pascalSmooth_previous[0][i-1]
        else:
            pascalDiff[0][i] = pascalSmooth_previous[0][i] - pascalSmooth_previous[0][i-1]

    return pascalDiff


def getSobeKernel(n):
    pascalSmoothKernel = pascalSmooth(n)
    pascalDiffKernel = pascalDiff(n)

    sobelKernel_x = singal.convolve2d(pascalSmoothKernel.transpose(), pascalDiffKernel, mode='full')
    sobelKernel_y = singal.convolve2d(pascalSmoothKernel, pascalDiffKernel.transpose(), mode='full')
    return (sobelKernel_x, sobelKernel_y)


def sobel(image, n):
    wors,cols =  image.shape
    pascalSmoothKernel = pascalSmooth(n)
    pascalDiffKernel = pascalDiff(n)

    image_sobel_x = signal.convolve2d(image, pascalSmoothKernel.transpose(), mode='same')
    image_sobel_x = signal.convolve2d(image_sobel_x,pascalDiffKernel,mode='same')

    image_sobel_y = signal.convolve2d(image, pascalSmoothKernel, mode='same')
    image_sobel_y = signal.convolve2d(image_sobel_y, pascalDiffKernel.transpose(), mode='same')

    return (image_sobel_x, image_sobel_y)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print("usage: python sobel.py imageFile")
        sys.exit(0)

    image_sobel_x,image_sobel_y = sobel(image,7)

    edge = np.sqrt(np.power(image_sobel_x,2.0)+np.power(image_sobel_y,2.0))

    edge = edge/np.max(edge)
    edge = np.power(edge,1)
    edge*=255
    edge = edge.astype(np.uint8)
    cv2.imshow('sobel edge', edge)
    cv2.imwrite('sobel.jpg',edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

