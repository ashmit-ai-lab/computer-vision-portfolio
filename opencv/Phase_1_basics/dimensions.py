import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    print("Dimensions = [H, W, C] =", image.shape)
else:
    print("No image found.")