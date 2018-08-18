# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal


if __name__ == "__main__":
    # 输入矩阵
    I = np.array([[1,2],[3,4]], np.float32)
    H1,W1 = I.shape[:2]
    print(H1,W1)
    K = np.array([[-1,-2],[2,1]], np.float32)
    H2,W2 = K.shape[:2]
    # 计算full卷积
    c_full = signal.convolve2d(I,K,mode='full')
    print(c_full)
