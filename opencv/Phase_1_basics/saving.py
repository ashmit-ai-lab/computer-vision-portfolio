import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    success = cv2.imwrite("Final.jpg", image)
    if success:
        print("Image saved successfully!")
    else:
        print("Image not saved.")
else:
    print("Image not found.")