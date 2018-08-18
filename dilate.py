# -*- coding: utf-8 -*-
import sys
import cv2


if __name__ ==  "__main__":
    if len(sys.argv)>1:
        I = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    else:
        print("Usage: python dilate.py imageFile")

    cv2.imshow("I", I)
    r = 1
    MAX_R = 20
    cv2.namedWindow("dilate", 1)
    def nothing(*arg):
        pass

    cv2.createTrackbar("r", "dilate", r, MAX_R,nothing)
    while True:
        r = cv2.getTrackbarPos("r", 'dilate')
        s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1))
        d = cv2.dilate(I, s)
        cv2.imshow("dilate", d)
        ch = cv2.waitKey(0)
        if ch == 27:
            break

    cv2.destroyAllWindows()

