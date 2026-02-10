import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''Morphological transformations are a set of operations that process images based on their shapes. 
They are typically applied to binary images, but can also be used on grayscale images.'''

'''A kernel decides the nature of the operation. It is a matrix of a certain size (e.g., 3x3, 5x5) that defines the neighborhood of pixels to be considered for the transformation.'''

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\smarties.png", 0)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2, 2), np.uint8)
# dilation is a morphological operation that adds pixels to the boundaries of objects in an image. It is used to expand the size of objects and fill in small holes or gaps in the foreground. The dilation operation works by taking the maximum pixel value in the neighborhood defined by the kernel and assigning it to the central pixel. This results in the expansion of the object boundaries, making them thicker and more connected. Dilation is commonly used in various applications such as noise removal, object detection, and image segmentation.
dilation = cv.dilate(mask, kernal, iterations=2)

# if kernal size is increased, the thickness of the object in the image will also increase after dilation operation, which will affect the overall appearance of the image. A larger kernel will result in a more pronounced dilation effect, making the objects in the image appear thicker and more connected. However, it may also lead to loss of fine details and increased noise in the image. Therefore, it is important to choose an appropriate kernel size based on the specific requirements of the application and the characteristics of the input image.

# erosion is a morphological operation that removes pixels from the boundaries of objects in an image. It is used to shrink the size of objects and remove small noise or unwanted details from the foreground. The erosion operation works by taking the minimum pixel value in the neighborhood defined by the kernel and assigning it to the central pixel. This results in the shrinking of the object boundaries, making them thinner and more disconnected. Erosion is commonly used in various applications such as noise removal, object detection, and image segmentation.
erosion = cv.erode(mask, kernal, iterations=2)

# opening is a morphological operation that is used to remove small noise or unwanted details from the foreground of an image. It is a combination of erosion followed by dilation. The opening operation works by first applying erosion to the image, which removes small noise and shrinks the object boundaries. Then, dilation is applied to the eroded image, which restores the original size of the objects while keeping the noise removed. This results in a cleaner and more refined image, making it easier to analyze and process. Opening is commonly used in various applications such as noise removal, object detection, and image segmentation.
# opening = erosion followed by dilation
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)

# closing is a morphological operation that is used to fill small holes or gaps in the foreground of an image. It is a combination of dilation followed by erosion. The closing operation works by first applying dilation to the image, which expands the object boundaries and fills in small holes or gaps. Then, erosion is applied to the dilated image, which restores the original size of the objects while keeping the holes filled. This results in a more connected and complete image, making it easier to analyze and process. Closing is commonly used in various applications such as noise removal, object detection, and image segmentation.
# closing = dilation followed by erosion
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)

# morphological gradient is a morphological operation that is used to highlight the edges of objects in an image. It is defined as the difference between the dilation and erosion of an image. The morphological gradient operation works by first applying dilation to the image, which expands the object boundaries and fills in small holes or gaps. Then, erosion is applied to the image, which shrinks the object boundaries and removes small noise or unwanted details. Finally, the difference between the dilated and eroded images is calculated, resulting in an image that highlights the edges of the objects. The morphological gradient is commonly used in various applications such as edge detection, object detection, and image segmentation.
# morphological gradient = dilation - erosion
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)

# top hat is a morphological operation that is used to extract small elements and details from an image. It is defined as the difference between the original image and its opening. The top hat operation works by first applying opening to the image, which removes small noise and shrinks the object boundaries. Then, the difference between the original image and the opened image is calculated, resulting in an image that highlights the small elements and details that were removed during the opening operation. The top hat operation is commonly used in various applications such as feature extraction, object detection, and image segmentation.
# top hat = original image - opening
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'morphological gradient', 'top hat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i], fontsize=5)
    plt.xticks([]), plt.yticks([])

plt.show()
