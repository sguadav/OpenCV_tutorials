import cv2

print("Opencv installed")

# Importing an image
"""
img = cv2.imread("images/instagram.png")
cv2.imshow("Output", img)
cv2.waitKey(2000)
"""

# Importing a video
"""
video = cv2.VideoCapture("images/CNBC.mp4")
while True:
    # Bool, the images
    success, img = video.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        """

# Using a webcam
video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)
video.set(10, 100)

while True:
    # Bool, the images
    success, img = video.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break