import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca citra dalam format grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Menampilkan histogram awal
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(image.ravel(), bins=256, range=[0, 256])
plt.title('Histogram Citra Awal')

# Melakukan Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Menampilkan hasil setelah equalization
plt.subplot(1, 2, 2)
plt.hist(equalized_image.ravel(), bins=256, range=[0, 256])
plt.title('Histogram Citra Setelah Equalization')

# Menampilkan citra asli dan citra setelah equalization
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

# Menyimpan citra hasil equalization
cv2.imwrite('equalized_image.jpg', equalized_image)

# Menunggu hingga tombol ditekan untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
