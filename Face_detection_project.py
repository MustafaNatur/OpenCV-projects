import cv2
import os

#The xml markup language is designed for convenient
# encoding and reading of information in a
# machine and manual way. The file structure
# and its parameters are specified using tags,
# attributes and preprocessors

#open xml file
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

path_to_data = 'Resources/Data_base'

#open img
img = cv2.imread('Resources/1.jpg')

#Set colour filter
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,1)


#set rectangle
n = 0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.putText(img, "FACE ", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)
    n = n + 1
    img_crop = img[y:y + h, x:x + w]
    cv2.imwrite(os.path.join(path_to_data, f'Face_{n}.jpg'), img_crop)

#show result
cv2.imshow('Result', img)
print(f'{n} people on the photo')



#delay
cv2.waitKey(0)





