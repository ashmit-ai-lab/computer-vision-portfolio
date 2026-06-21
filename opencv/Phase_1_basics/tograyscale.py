import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Converted successfully.")
    cv2.imshow("LOve", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image.")