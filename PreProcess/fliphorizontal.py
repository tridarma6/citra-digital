import cv2

image_path = 'gambar.jpeg'  
img = cv2.imread(image_path)

if img is None:
    print("Error: Gambar tidak ditemukan atau path salah.")
else:
    img_flip_horizontal = cv2.flip(img, 1)

    cv2.imshow('Flipped Image', img_flip_horizontal)
    
    cv2.imwrite('gambar_flip_horizontal.jpg', img_flip_horizontal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

