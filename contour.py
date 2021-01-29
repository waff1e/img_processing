import cv2
import numpy as np

img_color = cv2.imread('sample.jpg')
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_1 = (20, 20, 100)
upper_1 = (32, 255, 255)

lower_2 = (110, 30, 30)
upper_2 = (130, 255, 255)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

img_mask1 = cv2.inRange(img_hsv, lower_1, upper_1)
img_mask2 = cv2.inRange(img_hsv, lower_2, upper_2)

img_result1 = cv2.bitwise_and(img_gray, img_gray, mask = img_mask1)
img_result2 = cv2.bitwise_and(img_gray, img_gray, mask = img_mask2)

contours1, hierachy1 = cv2.findContours(img_result1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours2, hierachy2 = cv2.findContours(img_result2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for number in range(520, 600):
	cv2.drawContours(img_color, contours1, number, (0, 0, 255), 3)

cv2.drawContours(img_color, contours2, 492, (255, 0, 0), 3)

for number in range(520, 630):
	cv2.drawContours(img_color, contours2, number, (0, 255, 0), 3)

cv2.imshow('result', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
