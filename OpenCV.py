import cv2 as cv

img = cv.imread(".\images\screenshot_1.png", cv.IMREAD_COLOR)

cv.imshow("Display window", img)

k = cv.waitKey(0)
# cv.destroyAllWindows()