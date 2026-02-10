import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\messi5.jpg")
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

template = cv.imread(r"D:\Learning Notes and code\Opencv\images\messi_face.jpg", 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(grey_img, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv.imshow("image", img)
cv.imshow("template", template)

cv.waitKey(0)
cv.destroyAllWindows() 
