import cv2
import os

#The xml markup language is designed for convenient
# encoding and reading of information in a
# machine and manual way. The file structure
# and its parameters are specified using tags,
# attributes and preprocessors

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

#path to the save package
path_to_data = 'Resources/Data_base'

frameWidth = 1980
frameHeight = 1080

#capturing video from the camera
cap = cv2.VideoCapture('Resources/test_video.mp4')

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    imgCanny = cv2.Canny(img, 100, 100)
    n = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(img, "Face ", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)
        n = n + 1
        img_crop = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(path_to_data, f'Face_{n}.jpg'), img_crop)
    cv2.imshow("Result", img)

    #The Q button stops the video
    if cv2.waitKey(1) == ord('q'):
        break

