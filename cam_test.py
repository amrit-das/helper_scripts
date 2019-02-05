import cv2
import numpy as np 

try:
    index = int(sys.argv[1])
else:
    index = 0

cap = cv2.VideoCapture(index)
ret = True

while ret:
    ret, frame = cv2.VideoCapture(index)
    #algorithms below here

    cv2.imshow("Display",frame)
    if cv2.waitKey(1) == 27:
        break
    if cv2.waitKey(1) == ord('c'):
        cv2.imwrite("frame.png",frame)

cap.release()
cv2.destroyAllWindows()

