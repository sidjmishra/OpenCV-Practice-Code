import cv2
import numpy as np  

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
#         points.append((x, y))
#         if len(points) >= 2:
#             cv2.line(img, points[-1], points[-2], (255, 0, 0), 2)
#         # font = cv2.FONT_HERSHEY_SIMPLEX
#         # strXY = str(x) + "," + str(y)
#         # cv2.putText(img, strXY, (x,y), font, 1, (255, 255, 0), 2)
#         cv2.imshow("image", img)

# img = np.zeros((512, 512, 3), np.uint8)
# cv2.imshow("image", img)
# points = []

# cv2.setMouseCallback("image", click_event)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# --------------  click on any point on image and show color in second window

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)  
        mycolorimage = np.zeros((512, 512, 3), np.uint8)
        mycolorimage[:] = [blue, green, red]       
        cv2.imshow("color", mycolorimage)

img = cv2.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 1)
cv2.imshow("image", img)
points = []

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()




