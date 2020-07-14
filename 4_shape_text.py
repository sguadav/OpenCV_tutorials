import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# Figures
"""
img[200:300, 200:300] = 255, 0, 0           # all blue image
img[200:300, 200:300] = 255, 0, 0           # making a blue box    
"""

# Line
#       img, starting, ending,   color: RGB  , thick
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(img, (0, 0), (250, 250), (0, 0, 255), 2)
# filled rectangle
cv2.rectangle(img, (0, 0), (250, 250), (0, 0, 255), cv2.FILLED)

# Circle
cv2.circle(img, (350, 350), 100, (150, 150, 0), 2)

# Putting text
#                text,              start,          font,               size, RGB color
cv2.putText(img, "THIS IS PERFECT ", (300, 100), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 150, 255))

cv2.imshow("Image", img)

cv2.waitKey(0)
