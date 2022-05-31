import numpy as np
from PIL import Image


def Placement(N , Counter):
        cols = int(N/2)
        rows = 2
        size = 100, 100
        ims = []
        i = 1
        while i <= Counter:
            im = Image.open(f'{i}.jpg')
            im.thumbnail(size)
            new_im1 = Image.new('RGB', size, (255, 255, 255))
            new_im1.paste(im, (0, 0))

            ims.append(new_im1)
            i += 1

        new_im = Image.new('RGB', (100 * Counter, 200), (255, 255, 255))
        i = 0
        x = 0
        y = 0
        dx = 0
        k = 0

        while k < Counter // N + 1:
            for col in range(cols):
                for row in range(rows):
                    if i < Counter:
                        print(i, x, y)
                        new_im.paste(ims[i], (x, y))
                        i += 1
                        y = 100
                x += int((100 * Counter)/cols)
                y = 0
            dx += 100
            x = dx
            y = 0
            k += 1




        new_im.save("Collage.jpg")

