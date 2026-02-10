import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((200, 200), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (125), -1)

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 1)

# b,g,r = cv.split(img)
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)
# cv.imshow("img", img)

# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])

# calcHist() function calculates the histogram of an image. It takes the following parameters:
# images: A list of images for which the histogram needs to be calculated.
# channels: A list of channels for which the histogram needs to be calculated. For example, if you want to calculate the histogram for the blue channel, you would pass [0] as the channels parameter.
# mask: A mask image that specifies the region of interest for which the histogram needs to be calculated. If you want to calculate the histogram for the entire image, you can pass None as the mask parameter.

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()