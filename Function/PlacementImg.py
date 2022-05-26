import matplotlib.pyplot as plt
import cv2
def Placement(pictures, N):
    # creating an empty canvas
    pic_box = plt.figure(figsize=(20, 20))
    i=0
    for picture in pictures:
        # convert BGR img to RGB
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        # add a cell to pic_box to display a current page
        pic_box.add_subplot(1,N,i+1)
        plt.imshow(picture)
        # off axis
        plt.axis('off')
        plt.show()
        i+=1