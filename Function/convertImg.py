import cv2 as cv
import random as rd
def color_space_conv(image):
    N = rd.randint(0, 5)
    if N == 0:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.imshow("gray", gray)
        return gray
    if N == 1:
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        cv.imshow("hsv", hsv)
        return hsv
    if N == 2:
        yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
        cv.imshow("yuv", yuv)
        return yuv
    if N == 3:
        ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
        cv.imshow("Ycrcb", ycrcb)
        return ycrcb
    if N == 4:
        HIS = cv.cvtColor(image, cv.COLOR_BGR2HLS)
        cv.imshow("HIS", HIS)
        return HIS
    if N == 5:
        b, g, r = cv.split(image)
        B = float(b)
        G = float(g)
        R = float(r)
        channel = rd.randint(0, 2)
        rand = rd.randint(1, 9)
        if channel == 0:
            B = B / rand
            return cv.merge('RGB', (R, G, B))
        if channel == 1:
            G = G / rand
            return cv.merge('RGB', (R, G, B))
        if channel == 2:
            R = R / rand
            return cv.merge('RGB', (R, G, B))

