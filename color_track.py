import cv2
import numpy as np
center = None
y,u,v = 0,108,226
cap = cv2.VideoCapture(0)
pts = []

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while True:
	ret, frame = cap.read()
	img_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
	mask = cv2.inRange(img_yuv, (np.array([0,u-30,v-30])), (np.array([255,u+30,v+30])))
	im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

	if len(contours)>0:
		(x,y),radius = cv2.minEnclosingCircle(contours[0])
		if radius > 5:
			cv2.circle(frame, (int(x),int(y)), 5, (0, 0, 255), -1)
			center = int(x),int(y)

	pts.append(center)
	for i in range(1, len(pts)):
		try:
			cv2.line(frame, pts[i], pts[i+1], (255,0,0),2)
		except:
			continue			
	cv2.imshow("abc",frame)
	out.write(frame)
	if cv2.waitKey(1) == 27:
		cv2.imwrite("kedar_bhaiya.png",frame)
		break
out.release()
cap.release()
cv2.destroyAllWindows()





