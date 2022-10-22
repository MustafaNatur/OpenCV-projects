import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/car.png")
# DISPLAY
cv2.imshow("Show",img)
cv2.waitKey(0)