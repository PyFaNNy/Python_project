import cv2 as cv
import random as rd
import numpy as np
def color_space_conv(image):
        b, g, r = cv.split(image)
        channel = rd.randint(0, 2)
        rand = rd.randint(1, 9)
        if channel == 0:
            b = b / rand
            b = b.astype(np.uint8)
            return cv.merge([r, g, b])
        if channel == 1:
            g = (g / rand)
            g = g.astype(np.uint8)
            return cv.merge([r, g, b])
        if channel == 2:
            r = r / rand
            r = r.astype(np.uint8)
            return cv.merge([r, g, b])

