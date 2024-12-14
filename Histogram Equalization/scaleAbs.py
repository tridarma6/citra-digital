import cv2
import matplotlib.pyplot as plt

# Membaca citra
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Menyesuaikan kecerahan citra (penambahan nilai beta)
adjusted_image = cv2.convertScaleAbs(image, alpha=1, beta=50)  # alpha untuk kontras, beta untuk kecerahan

# Menampilkan citra hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Gambar Setelah Histogram Equalization")
plt.imshow(adjusted_image, cmap='gray')
plt.show()