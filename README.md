# OpenCV-projects
This is really big rep with OpenCV projects

# Main projects
* [Face detection](https://github.com/MustafaNatur/OpenCV-projects#Face-detection)
* [Warp perspective](https://github.com/MustafaNatur/OpenCV-projects#Warp-perspective)
* [Shapes detection](https://github.com/MustafaNatur/OpenCV-projects#Shapes-detection)
* [AR drawing](https://github.com/MustafaNatur/OpenCV-projects#AR-drawing)

# Learning projects
* [Cropping image](https://github.com/MustafaNatur/OpenCV-projects#Cropping-image)
* [Image stack](https://github.com/MustafaNatur/OpenCV-projects#Image-stack)
* [Images & video reading](https://github.com/MustafaNatur/OpenCV-projects#Images-&-video-reading)

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

'''
warpPerspective(source_image, result_image, outputimage_size)
'''

#### Steps

* set points coordinates on image (for example in Photoshop)
* make matrix for input data
* make matrix for output data
* use warp perspective function (OpenCV func)
* draw green lines and red points
* show result

#### Results

![animated_demo_screenshot](/Materials/Warp_perspective.jpg)
