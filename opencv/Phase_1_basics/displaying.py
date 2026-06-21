import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    cv2.imshow("Display", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Couldn't display image")