import cv2
import numpy as np
import datetime


cap = cv2.VideoCapture(0)  # 0 is the default camera
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set new width and height
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT)

# Or you can use the associated numeric values directly
cap.set(3, 1280)
cap.set(4, 720)
# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()  # ret is a boolean indicating if the frame was read successfully
    if ret:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()