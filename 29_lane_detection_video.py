import cv2 as cv    
import numpy as np

from matplotlib import pyplot as plt

def process(img):

    # define region of interest
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    region_of_interest_vertices = [
        (158,height),
        (width/2, height/2),
        (width, height)
    ]

    gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    canny_image = cv.Canny(gray_image, 100, 120)

    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(cropped_image, 2, np.pi/60, 50, np.array([]), 40, 100)

    image_with_lines = draw_the_lines(img, lines)
    return image_with_lines

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    # match_mask_color = (255,) * channel_count
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0,255,0), 4)
    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


cap = cv.VideoCapture(r"D:\Learning Notes and code\Opencv\images\test_video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()