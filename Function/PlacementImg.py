import  numpy as np
from PIL import Image


def Placement(N, Counter):
        cols = int(N/2)
        rows = 2
        width = 1200
        height = 800
        thumbnail_width = width // cols
        thumbnail_height = height // rows
        size = thumbnail_width, thumbnail_height
        new_im = Image.new('RGB', (width, height))
        ims = []
        i=1
        while i <=Counter:
            im = Image.open(f'{i}.jpg')
            im.thumbnail(size)
            ims.append(im)
            i+=1
        i = 0
        x = 0
        y = 0
        for col in range(cols):
            for row in range(rows):
                print(i, x, y)
                new_im.paste(ims[i], (x, y))
                i += 1
                y += thumbnail_height
            x += thumbnail_width
            y = 0

        new_im.save("Collage.jpg")