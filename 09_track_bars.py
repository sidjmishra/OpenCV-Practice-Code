import cv2
import numpy as np

# img = np.zeros((300, 512, 3), dtype="uint8")
# cv2.namedWindow("image")

# cv2.createTrackbar("B", "image", 0, 255, lambda x: print(x))
# cv2.createTrackbar("G", "image", 0, 255, lambda x: print(x))
# cv2.createTrackbar("R", "image", 0, 255, lambda x: print(x))


# switch = '0: OFF \n1: ON'
# cv2.createTrackbar(switch, "image", 0, 1, lambda x: print(x))


# while True:
#     cv2.imshow("image", img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:  # ESC key to exit
#         break

#     # get current positions of the trackbars
#     b = cv2.getTrackbarPos("B", "image")
#     g = cv2.getTrackbarPos("G", "image")
#     r = cv2.getTrackbarPos("R", "image")
#     s = cv2.getTrackbarPos(switch, "image")

#     if s == 0:
#         img[:] = 0  # turn off the color
#     else:
#         img[:] = [b, g, r]  # set the image color based on trackbar positions

# cv2.destroyAllWindows()


# ---------------------- example 2 ----------------------


cv2.namedWindow("image")

cv2.createTrackbar('CP', "image", 10, 400, lambda x: print(x))



switch = 'color/gray'
cv2.createTrackbar(switch, "image", 0, 1, lambda x: print(x))


while(1):
    img = cv2.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg")
    pos = cv2.getTrackbarPos('CP', "image")
    cv2.putText(img, str(pos), (10, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC key to exit
        break

    # get current positions of the trackbars

    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        pass 
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("image", img)
cv2.destroyAllWindows()