import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg")
cv.imshow("Original Image", img)

# matplotlib uses RGB format while OpenCV uses BGR format, so we need to convert the color space
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.xticks([])  # remove x-axis ticks
plt.yticks([])  # remove y-axis ticks
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()  