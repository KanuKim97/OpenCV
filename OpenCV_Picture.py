import cv2

img = cv2.imread('E:\python\OpenCV\sample.jpg', 1) //Upload your sample img

cv2.imshow('Test Img', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
