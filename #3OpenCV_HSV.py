import cv2

img_color = cv2.imread('E:\python\OpenCV\sample.jpg')
height,width = img_color.shape[:2]

img_HSV = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_blue = (120-10, 30, 30)
upper_blue = (120+10, 255, 255)
img_Mask= cv2.inRange(img_HSV, lower_blue, upper_blue)

img_Result = cv2.bitwise_and(img_color, img_color, mask = img_Mask)

cv2.imshow('img_color', img_color)
cv2.imshow('img_Mask', img_Mask)
cv2.imshow('img_result', img_Result)

cv2.waitKey(0)
cv2.destroyAllWindows()