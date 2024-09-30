import cv2
import numpy as np
# Baca gambar dan konversi ke grayscale
image = cv2.imread('gambar.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Dapatkan dimensi gambar
height, width = gray_image.shape
# Tentukan nilai threshold
threshold_value = 127
# Buat array kosong untuk gambar threshold hasil manual
threshold_image_manual = np.zeros((height, width), dtype=np.uint8)
# Loop melalui setiap piksel untuk melakukan thresholding manual
for i in range(height):
    for j in range(width):
        # Ambil nilai piksel dari gambar grayscale
        pixel_value = gray_image[i, j]
        # Terapkan threshold secara manual
        if pixel_value >= threshold_value:
            threshold_image_manual[i, j] = 255  # Putih
        else:
            threshold_image_manual[i, j] = 0    # Hitam
# Tampilkan gambar asli grayscale dan hasil threshold manual
cv2.imshow('Gambar Grayscale', gray_image)
cv2.imshow('Threshold Manual', threshold_image_manual)
# Tunggu hingga tombol ditekan untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
