import cv2 as cv    
import numpy as np

from matplotlib import pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\Road.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# define region of interest
print(img.shape)
height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [
    (158,height),
    (870,447),
    (width, height)
]

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

gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
canny_image = cv.Canny(gray_image, 100, 200)

cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

lines = cv.HoughLinesP(cropped_image, 6, np.pi/60, 160, np.array([]), 40, 25)

image_with_lines = draw_the_lines(img, lines)
plt.imshow(image_with_lines)

# plt.imshow(img)
# plt.imshow(cropped_image)

plt.show()