import cv2

a = cv2.imread('img/sample001.jpg')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
cv2.imshow('a', a)
cv2.waitKey(0)
cv2.destroyAllWindows()
