import cv2  #открыли нужную билиотеку

print('package important')#

img_darii = cv2.imread('Resources/1.jpg') # открываем кортинку и указываем путь к ней

imgGray = cv2.cvtColor(img_darii, cv2.COLOR_BGR2GRAY) # Изменение цветовой палитры картинки

imgBlur1 = cv2.blur(imgGray,(20,20)) # размытие изображения с разным ядром

imgCanny = cv2.Canny(imgGray, 100,100) # детектор границ Кенни Края(границы) — это такие кривые на изображении, вдоль которых
                                       # происходит резкое изменение яркости или других видов неоднородностей.
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur1", imgBlur1) # команда на вывод картинки блюр1
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)                   # задержка при показе картинки 1000 = 1 сек



