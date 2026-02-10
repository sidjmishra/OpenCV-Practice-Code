import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

''' image pyramids are a technique used in image processing and computer vision to create a multi-scale representation of an image.
They involve creating a series of images that are progressively smaller in size, with each level of the pyramid representing a 
different scale of the original image. The process of creating an image pyramid typically involves applying a low-pass filter to 
the original image and then downsampling it to create the next level of the pyramid. This process is repeated until a desired 
number of levels is reached or until the image size becomes too small. Image pyramids are commonly used in various applications 
such as image blending, object detection, and image compression, as they allow for efficient processing and analysis of images at 
different scales. By using image pyramids, we can capture both global and local features of an image, which can be beneficial for 
tasks such as feature extraction and object recognition.'''

'''
2 types of image pyramids:
1. Gaussian Pyramid: A Gaussian pyramid is created by applying a Gaussian filter to the image and then downsampling it. 
This process is repeated to create multiple levels of the pyramid, with each level representing a different scale of the original 
image. The Gaussian pyramid is commonly used for tasks such as image blending and multi-scale analysis.   

2. Laplacian Pyramid: A Laplacian pyramid is created by taking the difference between the original image and the Gaussian pyramid 
at each level. This results in a series of images that represent the high-frequency components of the original image at different 
scales. The Laplacian pyramid is often used for tasks such as image compression and edge detection, as it captures the details 
and edges of the image while discarding the low-frequency information.
'''
# Method 1
img = cv.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg")
# lr = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr)
# lr3 = cv.pyrDown(lr2)

# hr = cv.pyrUp(lr3)
# hr2 = cv.pyrUp(lr2)
# hr3 = cv.pyrUp(lr)

# cv.imshow("lena", img)
# cv.imshow("pyrDown", lr)
# cv.imshow("pyrDown2", lr2)
# cv.imshow("pyrDown3", lr3)
# cv.imshow("pyrUp", hr)
# cv.imshow("pyrUp2", hr2)
# cv.imshow("pyrUp3", hr3)

cv.waitKey(0)
cv.destroyAllWindows()

# Method 2
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)

# cv.waitKey(0)
# cv.destroyAllWindows()

# Laplacian Pyramid, no exclusive function for laplacian pyramid in opencv.
# difference between 2 consecutive layers in the gaussian pyramid gives us the laplacian pyramid.
layer = gp[5]
cv.imshow("upper level gaussian pyramid", layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i - 1], gaussian_expanded)
    lp.append(laplacian)
    cv.imshow(str(i), laplacian)

cv.waitKey(0)
cv.destroyAllWindows()