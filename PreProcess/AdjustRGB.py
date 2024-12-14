import cv2
import numpy as np

# Baca gambar
image_path = 'dog.jpeg'
img = cv2.imread(image_path)

# Pastikan gambar berhasil dibaca
if img is None:
    print("Gagal membaca gambar.")
    exit()

# Input nilai perubahan RGB dari user
r_change = int(input("Masukkan perubahan nilai R (misalnya -50 sampai 50): "))
g_change = int(input("Masukkan perubahan nilai G (misalnya -50 sampai 50): "))
b_change = int(input("Masukkan perubahan nilai B (misalnya -50 sampai 50): "))

# Terapkan perubahan dengan memastikan nilai tidak melebihi batas 0-255
img[:, :, 2] = np.clip(img[:, :, 2] + r_change, 0, 255)  # Kanal R (index 2)
img[:, :, 1] = np.clip(img[:, :, 1] + g_change, 0, 255)  # Kanal G (index 1)
img[:, :, 0] = np.clip(img[:, :, 0] + b_change, 0, 255)  # Kanal B (index 0)

# Tampilkan gambar asli dan hasil modifikasi
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Modified Image', img)

# Tunggu hingga user menekan tombol
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simpan gambar hasil modifikasi
cv2.imwrite('modified_image.jpeg', img)
print("Gambar berhasil disimpan sebagai 'modified_image.jpeg'.")
