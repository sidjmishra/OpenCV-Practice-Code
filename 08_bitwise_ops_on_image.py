import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), dtype="uint8")
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread(r"D:\Learning Notes and code\Opencv\images\3e846f05d9ddb50ea879b1bb216c186a.jpg")

# print(img2.shape)
# print(img1.shape)   
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# perdorm bitwise operations

#bitwise AND
bitwise_and = cv2.bitwise_and(img2, img1)
bitwise_or = cv2.bitwise_or(img2, img1)
bitwise_xor = cv2.bitwise_xor(img2, img1)
bitwise_not = cv2.bitwise_not(img2)
    
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
# cv2.imshow("Bitwise AND", bitwise_and)
# cv2.imshow("Bitwise OR", bitwise_or)
# cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()