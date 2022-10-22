import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,98),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # название картинки ее позиция размер цвет толщина
cv2.circle(img,(400,50),30,(255,255,0),5) # название картинки радиус  цвет толщина
cv2.putText(img,"Object detection", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3) # название изображения сам текст позиция размер цвет толщина надписи
cv2.imshow("img", img)
cv2.waitKey(0)