import cv2
import random


def scale(img):
    res = cv2.resize(img, None, fx=random.uniform(0.5, 1.3), fy=random.uniform(0.5, 1.3), interpolation=cv2.INTER_CUBIC)
    return res