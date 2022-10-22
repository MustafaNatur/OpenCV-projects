import cv2
import numpy as np

img = cv2.imread('Resources\BMW.jpg')
img_cropp = img[450:600,350:600]
print(img.shape)
cv2.imshow('BMW', img)
cv2.imshow('BMW crop', img_cropp)
cv2.waitKey(0)