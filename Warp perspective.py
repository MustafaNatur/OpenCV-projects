import cv2
import numpy as np

width, height = 740, 450

img1 = cv2.imread('Resources\Perspective.jpg')
#matrix
pts1 = np.float32([[75,236],[722,13], [364,600], [1062,251]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img1, matrix, (width, height))

# red points and green lines detected
cv2.circle(img1,(364,600), 9, (0, 0, 255), -1 )
cv2.circle(img1,(75,236), 9, (0, 0, 255), -1 )
cv2.circle(img1,(722,13), 9, (0, 0, 255), -1 )
cv2.circle(img1,(1062,251), 9, (0, 0, 255), -1 )
cv2.line(img1, (75, 236), (722, 13), (0, 255, 0), 3)
cv2.line(img1, (364, 600), (1062, 251), (0, 255, 0), 3)
cv2.line(img1, (75, 236), (364, 600), (0, 255, 0), 3)
cv2.line(img1, (722, 13), (1062, 251), (0, 255, 0), 3)



cv2.imshow("Show",img1)
cv2.imshow("perspective", result)
cv2.waitKey(0)