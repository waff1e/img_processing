import cv2

src = cv2.imread('img/sample001.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
print(gray.shape)

RGB = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
print(RGB.shape)
cv2.imshow('RGB', RGB)

cv2.waitKey(0)
cv2.destroyAllWindows()