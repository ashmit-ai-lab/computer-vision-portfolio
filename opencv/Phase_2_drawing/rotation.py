import cv2

image = cv2.imread(r"..\assets\Eggs.jpg")

if image is not None:
    (h, w) = image.shape[:2]

    center = (w//2, h//2) # w, h
    M = cv2.getRotationMatrix2D(center, 270, 1.0) # scale > 1 = zoom in, else zoom out

    rotated = cv2.warpAffine(image, M, (w, h))
    flipped = cv2.flip(image, -1) # 1 for hor flip, -1 for both flip

    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotated)
    cv2.imshow("Flipped", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image found.")