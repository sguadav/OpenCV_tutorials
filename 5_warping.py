import cv2
import numpy as np

img = cv2.imread("images/cards.jpg")
#img_resize = cv2.resize(img, (600, 450))

width, height = 250, 350
points1 = np.float32([[304, 73], [456, 69], [311, 261], [483, 253]])
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(points1, points2)
img_out = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Warp", img_out)

cv2.waitKey(0)

