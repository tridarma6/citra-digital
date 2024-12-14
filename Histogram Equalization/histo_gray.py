import cv2
import matplotlib.pyplot as plt

# Membaca gambar grayscale
image = cv2.imread('tst.jpg', cv2.IMREAD_GRAYSCALE)

# Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Gambar Setelah Histogram Equalization")
plt.imshow(equalized_image, cmap='gray')
plt.show()


