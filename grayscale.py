import cv2
import numpy as np

# Baca gambar berwarna
image = cv2.imread('gambar.jpeg')
# Dapatkan dimensi gambar
height, width, _ = image.shape
# Buat array kosong untuk gambar grayscale
gray_image_manual = np.zeros((height, width), dtype=np.uint8)
# Loop melalui setiap piksel untuk menghitung nilai grayscale
for i in range(height):
    for j in range(width):
        # Ambil nilai R, G, B dari gambar asli
        b, g, r = image[i, j]
        # Terapkan rumus grayscale manual
        gray_value = 0.299 * r + 0.587 * g + 0.114 * b
        # Set nilai grayscale ke gambar baru
        gray_image_manual[i, j] = gray_value

# Tampilkan gambar grayscale hasil manual
cv2.imshow('Grayscale Manual', gray_image_manual)

# Tunggu hingga tombol ditekan untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
