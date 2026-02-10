import cv2
import numpy as np  

# Itterate through all the attributes of cv2 and filter out those that contain 'EVENT' in their name
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

img = cv2.imread(r"D:\Learning Notes and code\Opencv\images\lena.jpg", 1)
# img = np.zeros((512, 512, 3), np.uint8) 
cv2.imshow("Mouse Events", img)

# Define a mouse callback function to handle mouse events
def mouse_event_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button down
        print(f"Left button down at ({x}, {y})")
        cv2.putText(img, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow("Mouse Events", img)
    elif event == cv2.EVENT_RBUTTONDOWN:  # Right mouse button down
        blue = img[y, x, 0]  # Get the blue channel value at the clicked position
        green = img[y, x, 1]  # Get the green channel value at the clicked position
        red = img[y, x, 2]  # Get the red channel value at
        cv2.putText(img, f"({blue}, {green}, {red})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        print(f"Right button down at ({x}, {y})")
        cv2.imshow("Mouse Events", img)

cv2.setMouseCallback("Mouse Events", mouse_event_handler)
cv2.waitKey(0)
cv2.destroyAllWindows()


