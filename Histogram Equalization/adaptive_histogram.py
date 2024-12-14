import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar berwarna
image = cv2.imread('image.jpg')

# Mengonversi gambar dari BGR ke RGB (karena OpenCV menggunakan BGR secara default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Mengubah gambar menjadi grayscale untuk CLAHE
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Membuat objek CLAHE dengan parameter tertentu
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Menerapkan CLAHE pada gambar grayscale
clahe_image = clahe.apply(gray_image)

# Menampilkan gambar asli dan gambar yang telah CLAHE dengan warna asli
plt.figure(figsize=(10, 5))

# Gambar asli (berwarna)
plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image_rgb)

# Gambar setelah CLAHE (berwarna)
# Mengonversi hasil CLAHE kembali ke gambar berwarna dengan cara menyatukan channel R, G, B asli
r, g, b = cv2.split(image)
r_clahe = clahe.apply(r)
g_clahe = clahe.apply(g)
b_clahe = clahe.apply(b)

# Menggabungkan kembali channel yang telah diberi CLAHE
clahe_color_image = cv2.merge((r_clahe, g_clahe, b_clahe))

# Menampilkan gambar CLAHE yang telah diterapkan pada gambar berwarna
plt.subplot(1, 2, 2)
plt.title("Gambar Setelah CLAHE")
plt.imshow(cv2.cvtColor(clahe_color_image, cv2.COLOR_BGR2RGB))

plt.show()