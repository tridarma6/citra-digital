import cv2
import numpy as np

# Membaca gambar
img = cv2.imread("gambar.jpeg")

# Mendapatkan dimensi gambar
height, width = img.shape[:2]

# Membuat array kosong untuk menyimpan gambar yang sudah diputar (90 derajat searah jarum jam)
rotate_90 = np.zeros((width, height, 3), dtype=np.uint8)
rotate_neg_90 = np.zeros((width, height, 3), dtype=np.uint8)
rotate_180 = np.zeros_like(img)

# Melakukan rotasi manual 90 derajat searah jarum jam
for x in range(width):
    for y in range(height):
        # Memindahkan piksel dari gambar asli ke gambar baru yang sudah diputar
        rotate_90[x, height - 1 - y] = img[y, x]

# Rotasi negatif 90 derajat
for x in range(width):
    for y in range(height):
        rotate_neg_90[width - 1 - x, y] = img[y, x]

# Rotasi 180 derajat
for x in range(width):
    for y in range(height):
        rotate_180[height - 1 - y, width - 1 - x] = img[y, x]

# Menampilkan gambar asli dan gambar yang sudah diputar
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image 90", rotate_90)
cv2.imshow("Rotated Image -90", rotate_neg_90)
cv2.imshow("Rotated Image 180", rotate_180)

# Tunggu hingga ada input dari pengguna untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()