'''Thresholding is a very popular technique for image segmentation. 
It is used to separate objects from the background in an image. 
The basic idea is to convert a grayscale image into a binary image, 
where the pixels are either black or white based on a certain threshold value. 
Compare each pixel value with the threshold and assign it to either 0 (black) or 255 (white) 
accordingly. This technique is widely used in various applications such as 
object detection, image analysis, and computer vision tasks.'''

import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\gradient.png", 0)

# simple thresholding
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
    
cv.imshow("Original Image", img)    
cv.imshow("Thresholded Image", th1)
cv.imshow("Thresholded Image Inverse", th2)
cv.imshow("Thresholded Image Trunc", th3)
cv.imshow("Thresholded Image ToZero Inv", th5)
cv.imshow("Thresholded Image ToZero", th4)

cv.waitKey(0)
cv.destroyAllWindows()