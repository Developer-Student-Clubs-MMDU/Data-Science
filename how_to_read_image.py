# Python code to read image
import cv2

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("img.png", cv2.IMREAD_COLOR)

#this will show the image
cv2.imshow("image", img)

# To hold the window on screen, we use cv2.waitKey method
 # 0 is an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)
