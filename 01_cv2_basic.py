import cv2
import numpy as np

# Read an image using OpenCV in Grayscale mode
img = cv2.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 0)
# print(img)

# Read an image using OpenCV in Color mode
# img_color = cv2.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 1)
# print(img_color)

# Display the images
cv2.imshow("Grayscale Image", img)
# cv2.imshow("Color Image", img_color)
# cv2.waitKey(0)
# #if you are using 64-bit machine, add & 0xFF after the waitKey() function to avoid overflow issues. For example: key = cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

# Save/Write the grayscale image to disk
# cv2.imwrite(r"D:\Learning Notes and code\Opencv\images\lena_saved_copy.jpg", img)

# Logic to destroy all windows when 'esc' key is pressed and save the image when 's' key is pressed
key = cv2.waitKey(0)
if key == 27:  # 27 is the ASCII value of 'esc'
    cv2.destroyAllWindows()
elif key == ord('s'): 
    cv2.imwrite(r"D:\Learning Notes and code\Opencv\images\lena_saved_copy.jpg", img)
    cv2.destroyAllWindows()

