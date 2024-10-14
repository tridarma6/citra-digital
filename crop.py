import cv2

image_path = 'gambar.jpeg' 
img = cv2.imread(image_path)

x1, y1, x2, y2 = 100, 100, 400, 400  
cropped_img = img[y1:y2, x1:x2]

cv2.imwrite('gambar_crop.jpeg', cropped_img)

cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
