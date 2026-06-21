import cv2
img = cv2.imread(r"..\assets\bird.jpg", cv2.IMREAD_GRAYSCALE) # Must be a grayscale

edges = cv2.Canny(img, 30, 200)

cv2.imshow("Original", img)
cv2.imshow("Canny_img", edges)

cv2.imwrite("Canny_edges.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()