import cv2

img = cv2.imread(r"..\assets\bird.jpg")

blur_img = cv2.medianBlur(img, 11)
cv2.imwrite("median_blur.jpg", blur_img)

cv2.imshow("Bird_org", img)
cv2.imshow("Blurredm_bird", blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()