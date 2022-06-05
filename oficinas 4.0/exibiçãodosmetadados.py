import cv2 as cv 
img = cv.imread('popeii.jpg', cv.IMREAD_UNCHANGED)
print(img.shape)
print(type(img))
print(img.dtype)