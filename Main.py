import cv2
from Function.RotateImage import Rotate
from Function.ConvertColorSpace import ConvertColorSpace
from Function.SaveImages import SaveImage
from Function.PlacementImg import Placement
# D:\Programming\Python\Python_project\original.jpg
path = input("Enter path to image:")
savePath = input("Enter path to save:")
number = int(input("Enter number of copy:"))

img = cv2.imread(path)
i=0
resultImg = []
while i < number:
    img = Rotate(img)
    img = ConvertColorSpace(img)
    resultImg.append(img)
    i+=1
Placement(resultImg, len(resultImg))
SaveImage(resultImg, savePath)
resultImg.count()