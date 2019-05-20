import numpy as np
from PIL import Image
from mss import mss
import cv2
import time

width=1920/2
height=1080/2

mon={'top':0,'left':0,'width':int(width),'height':int(height)}

sct=mss()

while "SCreen capturing":
	last_time=time.time()
	
	img=np.array(sct.grab(mon))
	
	cv2.imshow("OpenCV/Numpy normal", img)
	
	#print("fps: {0}".format(1/(time.time()-last_time)))
	
	if cv2.waitKey(25) & 0xFF == ord("q"):
		cv2.destroyAllWindows()
		break
		
		
#Webcam
#cap = cv2.VideoCapture(0)
#cap.open()
#print(cap.isOpened())
#while(cap.isOpened()):
#	ret, frame= cap.read()
#	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#	
#	cv2.imshow('frame',gray)
#	
#	if cv2.waitKey(1) &0xFF == ord('q'):
#		break
#	
#cap.release()
#cv2.destroyAllWindows()