import cv2
import numpy as np

img = cv2.imread(r"D:\Learning Notes and code\Opencv\opencv-4.x\samples\data\messi5.jpg")
img2 = cv2.imread(r"D:\Learning Notes and code\Opencv\opencv-4.x\samples\data\opencv-logo.png")
# # returns a tuple of number of rows, columns and channels in the image
# print(img.shape)

# # returns the total number of pixels in the image (rows x columns x channels)
# print(img.size)

# # returns the data type of the image (e.g., uint8 for 8-bit images)
# print(img.dtype)

# # split the image into its color channels (B, G, R)
# b,g,r = cv2.split(img)

# # merge the color channels back into a single image
# img = cv2.merge((b,g,r))

# cv2.imshow("image",img)
# cv2.waitKey(0)    
# cv2.destroyAllWindows()


#region of Interest (ROI)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r)) 
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


# resize images
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# add logo to the first image
# dst_img = cv2.add(img,img2)

# add weighted for blending two images depending on the alpha and beta values
dst_img_weighted = cv2.addWeighted(img,0.7,img2,0.3,0)

# cv2.imshow("image",dst_img)
cv2.imshow("image",dst_img_weighted)
cv2.waitKey(0)    
cv2.destroyAllWindows()