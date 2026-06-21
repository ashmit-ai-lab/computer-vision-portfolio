import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    centre = (264, 170)
    radius = 170
    color = (50, 200, 50)
    thickness = -1 #-1 fills cirecle with the color
    
    cv2.circle(image, centre, radius, color, thickness )
    cv2.imshow("image with circle", image)
    cv2.imwrite("With_circle.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image found.")