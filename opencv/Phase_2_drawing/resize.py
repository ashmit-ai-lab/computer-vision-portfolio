import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    print("Image loaded successfully.")
    
else:
    print("No image found.")

resized = cv2.resize(image, (224,224))
cv2.imshow("org", image)
cv2.imshow("Res", resized)
cv2.imwrite("Resized_img.jpg", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()