import cv2
import matplotlib.pyplot as plt

# Membaca gambar grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Membuat objek CLAHE dengan parameter batas kontras
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Menerapkan CLAHE pada gambar
clahe_image = clahe.apply(image)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Gambar Setelah CLAHE")
plt.imshow(clahe_image, cmap='gray')
plt.show()
