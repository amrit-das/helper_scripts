import cv2
import numpy as np
import sys

file_name = "video.mp4"
file_name = sys.argv[1]
cap = cv2.VideoCapture(file_name)
cnt = 0 

while (cap.isOpened()):
    cnt += 1
    ret, frame = cap.read()
    cv2.imwrite("frame{}.jpg".format(cnt), frame)
    if cv2.waitKey(20) == 27 or 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



