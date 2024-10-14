import cv2
import numpy as np

def adjust_contrast(img, alpha):
    # Mengubah gambar menjadi tipe float32 untuk menghindari overflow
    img_float = img.astype(np.float32)
    
    # Mengatur kontras dengan rumus: pixel = alpha * (pixel - 128) + 128
    contrasted_img = alpha * (img_float - 128) + 128
    
    # Memastikan nilai piksel tetap dalam rentang [0, 255]
    contrasted_img = np.clip(contrasted_img, 0, 255)
    
    # Mengembalikan tipe data ke uint8
    contrasted_img = contrasted_img.astype(np.uint8)
    
    return contrasted_img

img = cv2.imread("gambar.jpeg")

alpha = float(input("Masukkan nilai Contrast: "))
contrasted_img = adjust_contrast(img, alpha)

cv2.imshow("Original Image", img)
cv2.imshow("Contrasted Image", contrasted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
