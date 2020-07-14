import cv2
import numpy as np

img = cv2.imread("images/instagram.png")
print("(height, width, Channel)")
print(img.shape)

# Resizing
img_resize = cv2.resize(img, (450, 450))
print(img_resize.shape)

cv2.imshow("Normal", img)
cv2.imshow("Resized", img_resize)

# Cropping
# for matrix reference the height comes first an then the width
img_crop = img[0:300, 200:500]
cv2.imshow("Crop", img_crop)

cv2.waitKey(0)

