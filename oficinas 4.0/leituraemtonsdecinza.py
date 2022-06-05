import cv2 as cv 
from matplotlib import pyplot as plt
img = cv.imread('popeii.jpg', cv.IMREAD_UNCHANGED)
plt.imshow(img, cmap = 'gray')
plt.colorbar(cmap = 'gray', fraction=0.03, pad=0.04)
plt.show()