from PIL import Image
import random
def Rotate(img):
    deg = random.randint(1, 360);
    img_rotate = img.rotate(deg, expand=True)
    return img_rotate