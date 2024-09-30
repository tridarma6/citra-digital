import cv2
import numpy as np

image = cv2.imread('gambar.jpeg')
height, width, _ = image.shape
gray_image_manual = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        b, g, r = image[i, j]
        gray_value = 0.299 * r + 0.587 * g + 0.114 * b
        gray_image_manual[i, j] = gray_value

cv2.imshow('Grayscale Manual', gray_image_manual)

cv2.waitKey(0)
cv2.destroyAllWindows()
