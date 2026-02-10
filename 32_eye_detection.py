import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

face_cascade = cv.CascadeClassifier(r'D:\Learning Notes and code\Opencv\files\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(r'D:\Learning Notes and code\Opencv\files\haarcascade_eye_tree_eyeglasses.xml')

# Image detection
# img = cv.imread(r'D:\Learning Notes and code\Opencv\images\face.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# for (x, y, w, h) in faces:
#     cv.rectangle(img, (x, y), (x+w , y+h), (255, 0, 0), 4) 

# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# video detection
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w , y+h), (255, 0, 0), 4) 
        roi_gray = gray[y: y+h, x:x+w]
        roi_color = img[y: y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255, 0), 5)

    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
