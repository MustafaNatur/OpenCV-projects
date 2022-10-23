# OpenCV-projects
This is really big rep with OpenCV projects

# Main projects
* [Face detection](https://github.com/MustafaNatur/OpenCV-projects#Face-detection)
* [Warp perspective](https://github.com/MustafaNatur/OpenCV-projects#Warp-perspective)
* [Shapes detection](https://github.com/MustafaNatur/OpenCV-projects#Shapes-detection)
* [AR drawing](https://github.com/MustafaNatur/OpenCV-projects#AR-drawing)

# Learning projects
* [Cropping image](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Cropping%20img.py)
* [Image stack](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Joining%20images.py)
* [Images reading](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Imges_read.py)
* [Video reading](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Video_read.py)
* [Cropping image](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Cropping%20img.py)
* [Image operations](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Image%20operations.py)
* [Shapes](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Shapes.py)
* [Web camera read](https://github.com/MustafaNatur/OpenCV-projects/blob/main/Webcam_read.py)

# Face detection

This project detect faces in images as well as videos using Haar Cascades in OpenCV and Python.
The xml markup language is designed for convenient encoding and reading of information in a machine and manual way. The file structure and its parameters are specified using tags, attributes and preprocessors

#### Steps

* open xml file
* open img or video file
* set colour filter
* set rectangle
* show result
* the Q button stops the video

#### Results

![animated_demo_screenshot](/Materials/Face_detection_video.gif)

# Warp perspective

Sometimes the images or videos captured may not be выровнено для нас to view enough information from the images or videos, in such cases, it is necessary to align such images or videos to obtain better insights from the images or videos and in order to be able to change the perspective of the images or videos to получать more useful information from the images or videos, we make use of a function called getPerspectiveTransform() function and the changed perspective of the images or videos must be fit to the original images or videos and this can be done using a function called warpPerspective() function in OpenCV.

```
warpPerspective(input_image, output_image, outputimage_size)
```
#### Steps

* set points coordinates on image (for example in Photoshop)
* make matrix for input data
* make matrix for output data
* use warp perspective function (OpenCV func)
* draw green lines and red points
* show result

#### Results

![animated_demo_screenshot](/Materials/Warp_perspective.jpg)

# Shapes detection

In this project, I taught how to define the contours of shapes using OpenCV functions. After scanning the contours and vertices, it is determined what kind of shape is in the image. Filters for images are also implemented

#### Steps

* Use image with blur, grey colour 
 ```
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)
 ```
* make stack with our images
```
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
```
* find contours
```
def getContours:
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

```
* draw lines and points, print shapes's name
```
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)
```

#### Result

![animated_demo_screenshot](/Materials/Shapes_detection.jpg)


# AR drawing

In this project, the video is processed and the color in the frame is searched. Then, in place of this color, a dot of this color is placed. This way you can draw directly on the video stream. For this project, reading information from a webcam was used. (There are bugs in the work due to the quality of the image from the camera)

#### Result
![animated_demo_screenshot](/Materials/Drawing.gif)
