import cv2
import numpy as np
image = cv2.imread('gambar.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = gray_image.shape
threshold_value = 127
threshold_image_manual = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        pixel_value = gray_image[i, j]
        if pixel_value >= threshold_value:
            threshold_image_manual[i, j] = 255  
        else:
            threshold_image_manual[i, j] = 0    
cv2.imshow('Gambar Grayscale', gray_image)
cv2.imshow('Threshold Manual', threshold_image_manual)
cv2.waitKey(0)
cv2.destroyAllWindows()
