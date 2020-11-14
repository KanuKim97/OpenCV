import cv2

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size : {0}x{1}".format(width, height))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writter = cv2.VideoWriter('test.avi', fourcc, 24, (int(width), int(height)))

while cap.isOpened():
    success, frame = cap.read()
    if success:
        writter.write(frame)
        cv2.imshow('CAM1', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
writter.release()
cv2.destroyAllWindows()

