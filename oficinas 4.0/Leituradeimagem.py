import cv2 as cv 
img = cv.imread('popeii.jpg', cv.IMREAD_UNCHANGED)
cv.imshow('Pompeii city', img)
cv.waitKey(0)
cv.destroyAllWindows()