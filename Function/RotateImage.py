import cv2
import random
import imutils
def Rotate(img):
    count = random.randint(1, 360)
    img_rotate = imutils.rotate(img, count)
    return img_rotate