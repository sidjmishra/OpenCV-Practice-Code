import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

'''image gradient is a directional change in the intensity or color in an image. It is a fundamental concept in image processing and computer vision, as it helps to identify edges, contours, and other important features in an image. The gradient of an image can be calculated using various methods, such as the Sobel operator, Prewitt operator, or Scharr operator. These operators work by convolving the image with specific kernels that are designed to highlight changes in intensity in different directions (horizontal, vertical, or diagonal). The resulting gradient images can be used for tasks such as edge detection, feature extraction, and object recognition. By analyzing the gradients in an image, we can gain insights into the structure and content of the scene being captured.'''

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\sudoku.png", 0)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

''' sobely is used to detect vertical edges in an image, while sobelx is used to detect horizontal edges in an image.'''
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

SobelCombined = cv.bitwise_or(sobelX, sobelY)

''' scharr is a more accurate version of the sobel operator, which is used to detect edges in an image. It is designed to provide better results than the sobel operator, especially for images with high-frequency content. The scharr operator uses a larger kernel size (3x3) compared to the sobel operator (3x3), which allows it to capture more information about the edges in the image. The scharr operator is particularly effective for detecting edges in images with low contrast or noisy images, as it can help to enhance the edges while suppressing noise.'''

titles = ['image', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel Combined']
images = [img, lap, sobelX, sobelY, SobelCombined]
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i], fontsize=5)
    plt.xticks([]), plt.yticks([])

plt.show()