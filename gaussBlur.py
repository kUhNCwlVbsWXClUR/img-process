import sys
import numpy as np
from scipy import signal
import cv2

# @Author  : yugengde
# @File    : gaussBlur.py
# @Software: 
# @Description : 高斯平滑滤波

# Usage    python3 gaussBlur.py <image>
# 详细代码: opencv算法精解 第五章图像平滑
# @why 需要滤波: 每一幅图片都包含某种随机的噪声，噪声可以理解为某一种或多种原因造成的灰度值的随机变化，在大多是情况下通过平滑技术（也常称为滤波技术）进行抑制或者去除

def gaussBlur(image, sigma,H,W,_boundary='fill',_fillvalue=0):
    # 卷积核
    gaussKernel_x = cv2.getGaussianKernel(sigma,W,cv2.CV_64F)
    # 转置
    gaussKernel_x = np.transpose(gaussKernel_x)

    gaussBlur_x = signal.convolve2d(image,gaussKernel_x,mode='same',boundary=_boundary,fillvalue=_fillvalue)
    gaussKernel_y = cv2.getGaussianKernel(sigma,H,cv2.CV_64F)
    gaussBlur_xy = signal.convolve2d(gaussBlur_x, gaussKernel_y,mode='same', boundary=_boundary,fillvalue=_fillvalue)

    return gaussBlur_xy

if __name__ == "__main__":
    if len(sys.argv)>1:
        image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        cv2.imshow("image", image)
        blurImage = gaussBlur(image,5,51,51,'symm')
        blurImage = np.round(blurImage)
        blurImage = blurImage.astype(np.uint8)
        cv2.imshow('GaussBlur', blurImage)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Usage: python gaussBlur.py imageFile")
        sys.exit(0)

