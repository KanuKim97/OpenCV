import cv2

img = cv2.imread('E:\python\OpenCV\sample.jpg', 1)

cv2.imshow('Test Img', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
