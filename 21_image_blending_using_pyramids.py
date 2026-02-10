import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

''' image blending using pyramids is a technique used in image processing and computer vision to seamlessly blend two images together. It involves creating a multi-scale representation of the images using Gaussian and Laplacian pyramids, which allows for smooth transitions between the two images. '''
apple = cv.imread(r"D:\Learning Notes and code\Opencv\images\apple.jpg")
orange = cv.imread(r"D:\Learning Notes and code\Opencv\images\orange.jpg")

print(apple.shape)
print(orange.shape)

# create half of the apple and half of the orange
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# cv.imshow("apple", apple)
# cv.imshow("orange", orange)
# cv.imshow("apple_orange", apple_orange)

''' steps involved in image blending using pyramids:
1. Create Gaussian pyramids for both images: The first step is to create Gaussian pyramids for both images. This involves repeatedly applying a Gaussian filter to the images and downsampling them to create a series of images at different scales.   
2. Create Laplacian pyramids for both images: After creating the Gaussian pyramids, the next step is to create Laplacian pyramids for both images. This is done by taking the difference between each level of the Gaussian pyramid and the next level, which results in a series of images that represent the high-frequency components of the original images at different scales.
3. Blend the Laplacian pyramids: The next step is to blend the Laplacian pyramids of the two images together. This is typically done by taking a weighted average of the corresponding levels of the Laplacian pyramids, where the weights are determined by a blending mask that specifies how much of each image should be blended at each level.
4. Reconstruct the blended image: Finally, the blended image is reconstructed by summing up the blended Laplacian pyramid levels and adding them back to the corresponding levels of the Gaussian pyramid. This results in a seamless blend of the two images, where the transitions between them are smooth and natural. By using image pyramids, we can achieve a high-quality blend that preserves important features and details from both images while minimizing artifacts and distortions.  
'''

# generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy] 
for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generate Gaussian pyramid for orange
orange_copy = orange.copy() 
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

# generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# reconstruct the blended image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_reconstruct, apple_orange_pyramid[i])

cv.imshow("apple", apple)
cv.imshow("orange", orange)
cv.imshow("apple_orange", apple_orange)
cv.imshow("apple_orange_reconstruct", apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()