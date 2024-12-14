import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar berwarna
image = cv2.imread('tst.jpg')

# Mengonversi gambar dari BGR ke RGB (karena OpenCV menggunakan BGR secara default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Membagi gambar menjadi tiga channel warna (merah, hijau, biru)
r, g, b = cv2.split(image)

# Melakukan histogram equalization pada setiap channel
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)

# Menggabungkan kembali channel yang sudah dihitung equalization-nya
equalized_image = cv2.merge((r_eq, g_eq, b_eq))

# Menampilkan gambar asli dan gambar hasil equalization dengan warna asli
plt.figure(figsize=(10, 5))

# Gambar asli
plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image_rgb)

# Gambar setelah histogram equalization
plt.subplot(1, 2, 2)
plt.title("Gambar Setelah Histogram Equalization")
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))

plt.show()