import cv2
import random


def scale(img):
    image = cv2.imread(img)
    res = cv2.resize(image, None, fx=random.uniform(0.5, 2), fy=random.uniform(0.5, 2), interpolation=cv2.INTER_CUBIC)
    return res