import numpy as np
from PIL import Image
from mss import mss
import cv2
import time

width=1920-100
height=1080-100

with mss() as sct:
	monitor_number = 2
	mon=sct.monitors[monitor_number]
	
	monitor={
		"top": mon["top"],
		"left": mon["left"],
		"width": width,
		"height": height,
		"mon": monitor_number,
	}
	
	while "Screen capturing":
		last_time=time.time()
		
		img=np.array(sct.grab(monitor))
		
		cv2.imshow("OpenCV/Numpy normal",img)
		if cv2.waitKey(25) & 0xFF == ord("q"):
			cv2.destroyAllWindows()
			break

