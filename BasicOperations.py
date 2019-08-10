import cv2
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt 

img = cv2.imread('/home/ani/opencv_tut/Images/tiger.jpg',cv2.IMREAD_COLOR)
img[55,55] = [255,255,255]
px = img[55,55]
img[100:150, 100:150] = [255,255,255]
tiger_ear = img[37:111, 107:194]
img[0:74, 0:87] = tiger_ear
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

