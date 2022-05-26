import cv2
import os

def SaveImage(pictures, path):
    i =1
    for img in pictures:
        cv2.imwrite(os.path.join(path, f'{i}.jpg'), img)
        i+=1
