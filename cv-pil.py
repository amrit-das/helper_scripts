import cv2
from PIL import Image
import numpy as np
import sys

# PIL to openCV conversion
im = Image.open("/home/amrit/Desktop/SRM/codes/{}".format(sys.argv[1]))
im.show()
cv = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
cv2.imshow("cv",cv)
cv2.waitKey(0)

# OpenCV to PIL conversion
im = cv2.imread("/home/amrit/Desktop/SRM/codes/{}".format(sys.argv[1]))
cv = cv2.cvtColor(numpy.array(im), cv2.COLOR_BGR2RGB)
im = Image.fromarray(cv)
im.show()



