import cv2
import numpy as np

def rotate_image(img, angle):
    height, width = img.shape[:2]
    center = (width // 2, height // 2)
    # Mendapatkan matriks rotasi
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Menerapkan rotasi menggunakan warpAffine
    rotated = cv2.warpAffine(img, rotation_matrix, (width, height))
    return rotated

img = cv2.imread("gambar.jpeg")

angle = float(input("Masukkan nilai rotasi (derajat): "))

rotated_image = rotate_image(img, angle)

cv2.imshow("Original Image", img)
cv2.imshow(f"Rotated Image {angle} degrees", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
