import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    org = (70, 170)
    color = (255, 10, 50)
    thickness = 4
    text = "I love Eggs."

    cv2.putText(image, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, thickness)
    cv2.imshow("image with text", image)
    cv2.imwrite("With_text.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image found.")