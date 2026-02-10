import cv2
import numpy as np

# img = cv2.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 1)

# Draw a line on the image

# img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)  # Blue line with thickness 5

# create image using numpy zeros method
img = np.zeros([512, 512, 3], np.uint8) #(height, width, channels, data type)


# Pick RGB values front internet and insert here as BGR
img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 5)  # 44,96,147 picked from internet
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0,0,255), 5)  # 44,96,147 picked from internet
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # Green rectangle with thickness 3
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1)  # Red rectangle with thickness 3
img = cv2.circle(img, (447, 63), 63, (255, 0, 0), -1)  # Blue filled circle
img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)  # White text with thickness 5
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

