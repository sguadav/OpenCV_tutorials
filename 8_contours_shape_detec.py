import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 150:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            # Getting the box around an object
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            obj_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # To classify the image
            if obj_corners == 3:
                object_type = "Tri"
            elif obj_corners == 4:
                aspect_ratio = w/float(h)
                if 0.95 < aspect_ratio < 1.05:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif obj_corners > 6:
                object_type = "Circle"
            else:
                object_type = "Other"
            
            cv2.putText(img_contour, object_type,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_PLAIN, 0.8,
                        (0, 0, 0), 2)


# Importing an image
img = cv2.imread("images/shapes.jpg")
img_contour = img.copy()

# Find the shapes
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)

# Find the edges
img_canny = cv2.Canny(img_blur, 50, 50)
img_blank = np.zeros_like(img)

# Find contours
getContours(img_canny)

img_stack = stackImages(0.8, ([img, img_gray, img_blur], [img_canny, img_contour, img_blank]))

cv2.imshow("Output", img_stack)
cv2.waitKey(0)

