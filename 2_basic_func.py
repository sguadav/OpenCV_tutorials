import cv2
import numpy as np

img = cv2.imread("images/instagram.png")
kernel = np.ones((5, 5), np.uint8)

# Image to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bluring an image
#                                only odd number
img_blur = cv2.GaussianBlur(img_gray, (15, 15), 0)

# Finding the edges of pic
img_canny = cv2.Canny(img, 100, 100)

# Dilation
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

# Erode
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Gray", img_gray)
cv2.imshow("Blur", img_blur)
cv2.imshow("Canny", img_canny)
cv2.imshow("Dilation", img_dilation)
cv2.imshow("Erosion", img_eroded)
cv2.waitKey(0)
