#Video read for open cv
import cv2
#link to the path
cap = cv2.VideoCapture("Resources/test_video.mp4")
# loop for capturing frames
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
#when the 'q' button is pressed, the video turns off
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break