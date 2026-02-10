import cv2
import numpy as np

def nothing(x):
    pass    

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")

# create trackbars for adjusting the lower and upper bounds of the HSV color space for automatic color detection
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # create a mask using the defined color range
    mask = cv2.inRange(hsv, l_b, u_b)
    cv2.imshow("mask", mask)

    # apply the mask to the original image to extract the detected color regions
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        break   

cap.release()
cv2.destroyAllWindows()