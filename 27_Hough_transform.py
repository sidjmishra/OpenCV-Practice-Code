''' Hough Transform is a feature extraction technique used in image analysis, computer vision, and digital image processing. 
It is used to detect simple shapes such as lines, circles, and ellipses in an image. The Hough Transform works by transforming 
the image space into a parameter space, where each point in the parameter space corresponds to a specific shape in the image 
space. By analyzing the parameter space, we can identify the presence of specific shapes in the original image. The Hough 
Transform is particularly useful for detecting shapes that are partially obscured or noisy, making it a powerful tool for various 
applications such as object recognition, lane detection in autonomous vehicles, and medical imaging.'''

''' Hough transform algorithm steps:
1. Edge Detection: The first step in the Hough Transform algorithm is to perform edge detection.
2. Parameter Space Mapping: Each edge point in the image is mapped to a curve in the parameter space. For example, in the case of line detection, each edge point is mapped to a sinusoidal curve in the parameter space.
3. Accumulator Array: An accumulator array is created in the parameter space, where each cell
4. Conversion of infinite lines to finite lines'''

''' Hough lines methods:
1. Standard Hough Transform: This method detects lines in an image by transforming the edge points
2. Probabilistic Hough Transform: This method is a more efficient version of the standard Hough Transform, which uses a random sampling technique to reduce the number of edge points that need to be processed.
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\sudoku.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
# lines = cv.HoughLines(edges, 1, np.pi / 180, 200)

# for line in lines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
#     x1 = int(x0 + 1000 * (-b))
#     # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
#     y1 = int(y0 + 1000 * (a))
#     # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
#     x2 = int(x0 - 1000 * (-b))
#     # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
#     y2 = int(y0 - 1000 * (a))
#     cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

# cv.imshow("image", img)


# Method 2: Probabilistic Hough Transform
lines = cv.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()