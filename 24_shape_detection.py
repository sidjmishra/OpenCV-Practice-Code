import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\shapes.png")
imgrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(imgrey, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 255), 5)
    # ravel method flattens the array and gives us the x and y coordinates of the contour points.
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspectRatio = float(w) / h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)


cv.imshow("shapes", img)
cv.waitKey(0)
cv.destroyAllWindows()