import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\gradient.png", 0)

# simple thresholding
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ["Original Image", "Simple Thresholding", "Thresholded Image Inverse", "Thresholded Image Trunc", "Thresholded Image ToZero Inv", "Thresholded Image ToZero"]
images = [img, th1, th2, th3, th5, th4]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i], fontsize=5)
    plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()