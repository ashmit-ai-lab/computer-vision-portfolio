import cv2
import numpy as np
img = cv2.imread(r"..\assets\camel.jpg")

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharp_img = cv2.filter2D(img, 0, kernel)

cv2.imwrite("sharp_camel.jpg", sharp_img)

cv2.imshow("Org_img", img)
cv2.imshow("Sharp_img", sharp_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
