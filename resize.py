import cv2
import numpy as np
import sys

image = sys.argv[1]

img = cv2.imread(image)
size = (int(sys.argv[2]),int(sys.argv[3]))
res = cv2.resize(img, size)
cv2.imwrite("output1.jpg",res)
cv2.waitKey(0)
