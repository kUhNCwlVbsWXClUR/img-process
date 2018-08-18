# -*- coding: utf-8 -*-
import sys
import cv2


if __name__ == "__main__":
    if len(sys.argv)>1:
        I = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print("Usage: python erode.py imageFile")

    s = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    r = cv2.erode(I,s)
    e = I - r
    cv2.imshow("I", I)
    cv2.imshow("erode", r)
    cv2.imshow("edge", e)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
