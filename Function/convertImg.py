import cv2 as cv

def color_space_conv(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb",Ycrcb)
    HIS = cv.cvtColor(image,cv.COLOR_BGR2HLS)
    cv.imshow("HIS",HIS)