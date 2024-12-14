import cv2
import numpy as np

def adjust_brightness(img, brightness_value):
    # Mengubah gambar menjadi tipe float untuk mencegah overflow/underflow saat menambah kecerahan
    img_float = img.astype(np.float32)
    
    # Menambahkan nilai brightness ke semua piksel
    brightened_img = img_float + brightness_value
    
    # Memastikan nilai piksel tetap dalam rentang [0, 255]
    brightened_img = np.clip(brightened_img, 0, 255)
    
    # Mengembalikan tipe data ke uint8
    brightened_img = brightened_img.astype(np.uint8)
    
    return brightened_img

img = cv2.imread("gambar.jpeg")

brightness_value = int(input("Masukkan nilai Brightness (-255 hingga 255): "))
brightened_img = adjust_brightness(img, brightness_value)

cv2.imshow("Original Image", img)
cv2.imshow("Brightened Image", brightened_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
