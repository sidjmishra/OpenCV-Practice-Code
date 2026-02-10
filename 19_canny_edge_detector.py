''' canny edge detector is a multi-stage algorithm that detects edges in an image by looking for areas of rapid intensity change. 
The algorithm consists of several steps, including noise reduction, gradient calculation, non-maximum suppression, and edge 
tracking by hysteresis. The canny edge detector is widely used in computer vision applications such as object detection, 
image segmentation, and feature extraction due to its ability to produce clean and accurate edge maps while minimizing the 
effects of noise.
steps involved in canny edge detection:
1. Noise Reduction: The first step in the canny edge detection algorithm is to reduce noise in the image. This is typically done using a Gaussian filter, which helps to smooth the image and reduce the impact of noise on edge detection.
2. Gradient Calculation: After noise reduction, the algorithm calculates the gradient of the image using techniques such as the Sobel operator. This step helps to identify areas of rapid intensity change, which are potential edges in the image.
3. Non-Maximum Suppression: In this step, the algorithm performs non-maximum suppression to thin the edges. It compares the gradient magnitude of each pixel with its neighbors in the direction of the gradient. If the pixel's gradient magnitude is not greater than its neighbors, it is suppressed (set to zero).
4. Double Thresholding: The algorithm applies a double threshold to classify the edges into three categories: strong edges, weak edges, and non-edges. Strong edges are those with a gradient magnitude above the high threshold, weak edges are those with a gradient magnitude between the low and high thresholds, and non-edges are those with a gradient magnitude below the low threshold.
5. Edge Tracking by Hysteresis: The final step involves edge tracking by hysteresis, where the algorithm connects the edges based on a high and low threshold. If a pixel's gradient magnitude is above the high threshold, it is considered a strong edge. If it is between the low and high thresholds, it is considered a weak edge. The algorithm then tracks the edges by connecting strong edges and weak edges that are connected to strong edges, while discarding weak edges that are not connected to any strong edges. This helps to produce a clean and accurate edge map while minimizing the effects of noise.
'''

import cv2 as cv
import numpy as np  

import matplotlib.pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\messi5.jpg", 0)
'''threshold1 is the lower threshold and threshold2 is the upper threshold for the hysteresis procedure.'''
canny = cv.Canny(img, 100, 200)
titles = ['image', 'canny edges']

images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i], fontsize=5)
    plt.xticks([]), plt.yticks([])

plt.show()