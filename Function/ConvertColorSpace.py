import numpy as np
import random

#read image
def ConvertColorSpace(img):
    rgb = random.randint(1, 3);
    if rgb == 1:
        img[:,:,0] = np.zeros([img.shape[0], img.shape[1]])
    if rgb == 2:
        img[:, :, 2] = np.zeros([img.shape[0], img.shape[1]])
    if rgb == 3:
        img[:, :, 1] = np.zeros([img.shape[0], img.shape[1]])
    return img