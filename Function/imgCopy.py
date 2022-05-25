import cv2
import numpy
import os
from pathlib import Path
def Copy(img, number):
    image_copies = []
    i = 0
    while i < number:
        image_copies.append(img)
        i = i + 1
        cv2.imshow(img)
    return image_copies