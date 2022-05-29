import matplotlib.pyplot as plt
import os
def Placement(pictures, N):
    pictures = os.listdir('pic')
    pictures = sorted(pictures)
    background = plt.figure(figsize=(100, 100))
    for i, picture in N:
        (width, height) = picture.size
        x = (100/N*i - width/2)
        y = 50
        background.paste(picture, (x, y))
        i+=1
        return background
