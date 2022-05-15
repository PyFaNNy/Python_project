import cv2
import random
def Rotate(img):
    count = random.randint(0, 3);
    for i in range(count):
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return img