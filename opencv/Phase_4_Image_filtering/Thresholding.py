import cv2
img = cv2.imread(r"..\assets\camel.jpg", cv2.IMREAD_GRAYSCALE) # Must be a grayscale

ret, thresh_img = cv2.threshold(img, 145, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Thresh_img", thresh_img)
cv2.imwrite("Thresh.jpg", thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()