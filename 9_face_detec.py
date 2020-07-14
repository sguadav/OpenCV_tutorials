import cv2

# Cascade detects all kind of things, research about this
face_cascade = cv2.CascadeClassifier("images/haarcascade_frontalface_default.xml")
# Importing an image
img = cv2.imread("images/person5.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get faces:                        might change
faces = face_cascade.detectMultiScale(img_gray, 1.25, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow("Output", img)
cv2.waitKey(2000)