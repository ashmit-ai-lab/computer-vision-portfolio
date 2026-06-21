import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    print("Image loaded successfully.")
    print(image.shape)
    cropped = image[50:339, 100:509]
    cv2.imshow("Original", image)
    cv2.imshow("Cropped", cropped)
    cv2.imwrite("Cropped_img.jpg", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image found.")