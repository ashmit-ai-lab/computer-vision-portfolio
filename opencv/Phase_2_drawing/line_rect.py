import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    pt1 = (10, 330)
    pt2 = (500, 10)

    ptr1 = (10, 10)
    ptr2 = (500, 330)

    color = (200, 100, 100)
    thickness = 6
    cv2.line(image, pt1, pt2, color, thickness)
    cv2.rectangle(image, ptr1, ptr2, color, thickness)
    cv2.imshow("image with line and rect", image)
    cv2.imwrite("With_line_rect.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image found.")