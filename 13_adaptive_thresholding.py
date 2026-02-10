'''Adaptive Thresholding is a more advanced technique for image segmentation that allows for varying lighting conditions in an image. 
Unlike simple thresholding, which uses a global threshold value for the entire image, adaptive thresholding calculates the threshold for each pixel based on the local neighborhood of that pixel. This is particularly useful in situations where the lighting is uneven across the image, as it can help to better separate the foreground from the background. 
Adaptive thresholding can be implemented using different methods, such as the mean and Gaussian methods.'''

import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\sudoku.png", 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# adaptive thresholding. adaptive_thresh_mean_c calculates the mean of the neighborhood area and subtracts a constant C from it to determine the threshold for each pixel.
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# # adaptive_thresh_gaussian_c calculates a weighted sum of the neighborhood values where the weights are a Gaussian window, and then subtracts a constant C from it to determine the threshold for each pixel.
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)        

cv.imshow("Original Image", img)
cv.imshow("Simple Thresholding", th1)
cv.imshow("Adaptive Mean Thresholding", th2)
cv.imshow("Adaptive Gaussian Thresholding", th3)

cv.waitKey(0)
cv.destroyAllWindows()