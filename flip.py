import cv2
import numpy as np

img = cv2.imread("gambar.jpeg")
height, width = img.shape[:2]

# Flip Vertikal (Atas ke Bawah)
flip_vertical = np.zeros_like(img)
for x in range(width):
    for y in range(height):
        flip_vertical[height - 1 - y, x] = img[y, x]

cv2.imshow("Gambar asli", img)

cv2.imshow("Flipped Vertical", flip_vertical)

# Flip Horizontal (Kiri ke Kanan) 
flip_horizontal = np.zeros_like(img)
for x in range(width):
    for y in range(height):
        flip_horizontal[y, width - 1 - x] = img[y, x]

cv2.imshow("Flipped Horizontal", flip_horizontal)

cv2.waitKey(0)
cv2.destroyAllWindows()
