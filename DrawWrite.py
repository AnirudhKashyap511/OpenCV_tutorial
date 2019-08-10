import cv2
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt 
img = cv2.imread('/home/ani/opencv_tut/Images/tiger.jpg',cv2.IMREAD_COLOR)
#the parameters are the image, the x coordinate the y coordinate, the color, pixelsize
#colors are in the order BGR and not RGB
cv2.line(img, (0,0), (550,500), (0,255,0), 15)
cv2.rectangle(img, (15,25), (200,150), (0,255,255), 5) 
#The parameter -1 fills the circle  
cv2.circle(img, (100,63), 55, (255,0,0), -1)
pts = np.array([[10,5],[20,30],[70,20],[50,20]],np.int32)
pts = pts.reshape((-1,1,2))
#The true here, connects the final point to the first point
#tThe last parameter is the pixel size
cv2.polylines(img,[pts],True,(0,0,255), 5)
# 1 is the font size, 2 is the spacing between letters, AA- Anti Aliasing
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorial',(0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
