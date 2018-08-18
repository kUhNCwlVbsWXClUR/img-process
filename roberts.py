from scipy import signal
import sys
import cv2
import numpy as np


def roberts(I, _boundary='fill', _fillvalue=0):
    H1,W1 = I.shape[0:2]
    H2,W2 = 2,2
    # 卷积核1
    R1 = np.array([[1,0],[0,-1]],np.float32)
    kr1,kc1 = 0,0
    # 计算full卷积
    IconR1 = signal.convolve2d(I,R1,mode='full',boundary=_boundary,fillvalue=_fillvalue)
    IconR1 = IconR1[H2-kr1-1:H1+H2-kr1-1,W2-kc1-1:W1+W2-kc1-1]

    # 卷积核2
    R2 = np.array([[0,1],[-1,0]], np.float32)
    IconR2 = signal.convolve2d(I, R2, mode='full',boundary=_boundary, fillvalue=_fillvalue)
    kr2,kc2 = 0,1
    IconR2 = IconR2[H2-kr2-1:H1+H2-kr2-1,W2-kc2-1:W1+W2-kc2-1]

    return (IconR1, IconR2)


if __name__ ==  "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print("Usage: python roberts.py imageFile")
        sys.exit(0)

    cv2.imshow('image', image)

    IconR1,IconR2 = roberts(image,'symm')
    IconR1 = np.abs(IconR1)
    edge_45 = IconR1.astype(np.uint8)
    #cv2.imshow('edge_45', edge_45)

    # bin
    ret,thresh55 = cv2.threshold(edge_45,55,255,cv2.THRESH_BINARY_INV)
    ret,thresh45 = cv2.threshold(edge_45,45,255,cv2.THRESH_BINARY_INV)
    ret,thresh35 = cv2.threshold(edge_45,35,255,cv2.THRESH_BINARY_INV)
    ret,thresh25 = cv2.threshold(edge_45,25,255,cv2.THRESH_BINARY_INV)
    th2 = cv2.adaptiveThreshold(edge_45, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

    #cv2.imshow('thresh55', thresh55)
    #cv2.imshow('thresh45', thresh45)
    #cv2.imshow('thresh35', thresh35)
    cv2.imshow('thresh25', thresh25)
    #cv2.imshow('th2', th2)


    IconR2 = np.abs(IconR2)
    edge_135 = IconR2.astype(np.int8)
    #cv2.imshow('edge_135',edge_135)

    # 用方平和的开方来衡量最后输出的边缘
    edge = np.sqrt(np.power(IconR1,2.0)+np.power(IconR2,2.0))
    edge = np.round(edge)
    edge[edge>255] = 255
    edge = edge.astype(np.int8)
    cv2.imshow('edge', edge)

    #cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

