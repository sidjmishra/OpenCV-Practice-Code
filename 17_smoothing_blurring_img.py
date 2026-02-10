''' linear filtering is a technique used in image processing to modify an image by applying a linear transformation to its pixel values. 
It involves convolving the image with a kernel, which is a small matrix that defines the weights
Homogeneous linear filters are a type of linear filter where the kernel is normalized, meaning that the sum of its elements is equal to 1.
This normalization ensures that the overall intensity of the image is preserved after filtering, preventing any unintended bright
Gaussian filters are a type of linear filter that uses a Gaussian function as the kernel. The Gaussian function is defined by its mean and standard deviation, which control the shape and spread of the kernel. Gaussian filters are commonly used for smoothing and blurring images, as they effectively reduce noise while preserving edges and details. The weights in a Gaussian kernel decrease exponentially as the distance from the center increases, giving more importance to nearby pixels and less to distant ones. This results in a smooth and natural blurring effect, making Gaussian filters a popular choice for various image processing applications.
Median filters are a type of non-linear filter that replaces each pixel value in an image with the median value of its neighboring pixels. The median is the middle value when the neighboring pixel values are sorted in order. This filtering technique is particularly effective for removing salt-and-pepper noise, which consists of random occurrences of black and white pixels in an image. Unlike linear filters, median filters do not blur edges and details as much, making them a good choice for preserving important features in an image while reducing noise. Median filters are commonly used in various applications such as image denoising, edge preservation, and object detection.
Bilateral filters are a type of non-linear filter that is used for edge-preserving smoothing of images. They work by combining both spatial and intensity information to determine the weights for filtering. The bilateral filter considers both the spatial distance between pixels and the intensity difference between them when calculating the weights for averaging. This allows it to effectively reduce noise while preserving edges and details in the image. The bilateral filter is particularly useful in applications such as image denoising, edge detection, and image enhancement, where it can help to improve the visual quality of the image without sacrificing important features.'''

import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\opencv-logo.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img2 = cv.imread(r"D:\Learning Notes and code\Opencv\images\Halftone_Gaussian_Blur.jpg", 0)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

img3 = cv.imread(r"D:\Learning Notes and code\Opencv\images\Noise_salt_and_pepper.png", 0)
img3 = cv.cvtColor(img3, cv.COLOR_BGR2RGB)

img4 = cv.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 0)
img4 = cv.cvtColor(img4, cv.COLOR_BGR2RGB)

# kernel formula = 1/(size of kernel) * np.ones((size of kernel, size of kernel), np.float32)
# size of kernel = 5, so kernel formula = 1/25 * np.ones((5, 5), np.float32)
kernel = np.ones((5, 5), np.float32) / 25

# destination image after applying the filter
dst = cv.filter2D(img, -1, kernel)

dst2 = cv.filter2D(img2, -1, kernel)

dst3 = cv.filter2D(img3, -1, kernel)

''' As 1-D signals, Images can also be filtered with various low-pass, high-pass, and band-pass filters.
lpf = low-pass filter helps to remove noise and blur the image
hpf = high-pass filter helps to enhance edges and details in the image.'''

''' Methods available in OpenCV for blurring/smoothing images:
1. cv.blur() - A simple averaging filter that takes the average of all the pixels in the kernel area and replaces the central pixel with this average value. It is a basic low-pass filter that can be used for general blurring and noise reduction.'''

blur = cv.blur(img, (5, 5))
blur2 = cv.blur(img2, (5, 5))

'''Gaussian Filter uses different weights for different pixels in the kernel area, giving more importance to the central pixels and less to the distant ones. This results in a smoother and more natural blurring effect compared to the simple averaging filter. The Gaussian filter is particularly effective for reducing noise while preserving edges and details in the image.
formula for Gaussian filter = 1/16 * np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])'''

gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)
gaussian_blur2 = cv.GaussianBlur(img2, (5, 5), 0)

''' median blur is a non-linear filter that replaces each pixel value in an image with the median value of its neighboring pixels. The median is the middle value when the neighboring pixel values are sorted in order. This filtering technique is particularly effective for removing salt-and-pepper noise, which consists of random occurrences of black and white pixels in an image. Unlike linear filters, median filters do not blur edges and details as much, making them a good choice for preserving important features in an image while reducing noise. Median filters are commonly used in various applications such as image denoising, edge preservation, and object detection.'''

median_blur = cv.medianBlur(img3, 5)

''' bilateral filter is a non-linear filter that is used for edge-preserving smoothing of images. They work by combining both spatial and intensity information to determine the weights for filtering. The bilateral filter considers both the spatial distance between pixels and the intensity difference between them when calculating the weights for averaging. This allows it to effectively reduce noise while preserving edges and details in the image. The bilateral filter is particularly useful in applications such as image denoising, edge detection, and image enhancement, where it can help to improve the visual quality of the image without sacrificing important features.'''
bilateral_blur = cv.bilateralFilter(img4, 9, 75, 75)

# titles = ['image', '2D Convolution', 'blur', 'gaussian blur']
# images = [img, dst, blur, gaussian_blur]

titles2 = ['image', '2D Convolution', 'blur', 'gaussian blur', 'median blur', 'bilateral blur']
images2 = [img2, dst2, blur2, gaussian_blur2, median_blur, bilateral_blur]

# for i in range(4):
#     plt.subplot(1, 4, i + 1)
#     plt.imshow(images[i], "gray")
#     plt.title(titles[i], fontsize=5)
#     plt.xticks([]), plt.yticks([])

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images2[i], "gray")
    plt.title(titles2[i], fontsize=5)
    plt.xticks([]), plt.yticks([])

plt.show()
