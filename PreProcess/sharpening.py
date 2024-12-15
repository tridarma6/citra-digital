import cv2
import numpy as np

def sharpen_image(img):
    # Membuat kernel sharpening
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    # Melakukan filtering gambar menggunakan kernel sharpening
    sharpened_img = cv2.filter2D(img, -1, kernel)
    
    return sharpened_img

img = cv2.imread("gambar.jpeg")

sharpened_img = sharpen_image(img)

cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
