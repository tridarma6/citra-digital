import cv2
import numpy as np

# Baca gambar dari file
image = cv2.imread('gambar.jpeg')

# Tampilkan gambar asli
cv2.imshow('Gambar Asli', image)

# Konversi gambar ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gambar Grayscale', gray_image)

# Lakukan Thresholding
_, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Gambar Threshold', threshold_image)

# Deteksi tepi menggunakan Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)
cv2.imshow('Deteksi Tepi (Canny)', edges)

# Tunggu hingga tombol ditekan untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
