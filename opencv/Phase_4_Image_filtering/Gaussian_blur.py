import cv2

img = cv2.imread(r"..\assets\bird.jpg")

blur_img = cv2.GaussianBlur(img, (11,11), 2) # sigma = 0 for auto blur
cv2.imwrite("gauss_blur.jpg", blur_img)

cv2.imshow("Bird_org", img)
cv2.imshow("Blurred_bird", blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()