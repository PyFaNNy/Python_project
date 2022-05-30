import cv2
from Function.RotateImage import Rotate
from Function.ConvertColorSpace import ConvertColorSpace
from Function.convertImg import color_space_conv
from Function.SaveImages import SaveImage
from Function.PlacementImg import Placement
from Function.ScaleImage import scale
# D:\Programming\Python\Python_project\original.jpg
# D:\Programming\Python\Python_project\123.jpg
path = input("Enter path to image:").split(" ")
savePath = input("Enter path to save:")
number = int(input("Enter number of copy:"))


i=0
resultImg = []
for p in path:
    img = cv2.imread(p)
    while i < number:
        img = Rotate(img)
        img = color_space_conv(img)
        img = scale(img)
        resultImg.append(img)
        i+=1
    i=0
SaveImage(resultImg, savePath)
listOfImages=['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']
Placement(listOfImages[:len(path)*number],len(path)*number)