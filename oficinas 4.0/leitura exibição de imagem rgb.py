import cv2 as cv
from cv2 import IMREAD_UNCHANGED
img = cv.imread('street market italy.jpg', cv.IMREAD_UNCHANGED )
cv.imshow('Street market italy 1', img)
print(img.shape)
print(type(img))
print(img.dtype)
cv.waitKey(0)
cv.destroyAllWindows()