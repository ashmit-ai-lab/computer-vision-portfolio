import cv2

# img = cv2.imread(r"..\assets\triangle.png")
img = cv2.imread(r"..\assets\shapes.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)

# Find Contours
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# RETR_TREE for all contours, CHAIN_APPROX_SIMPLE for lesser details

# Draw contours
cv2.drawContours(img, contours, -1, (255, 0, 0), 3) # BGR

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    corners = len(approx)

    if corners == 3:
        shape_name = "triangle"

    elif corners == 4:
        shape_name = "rectangle"

    elif corners == 6:
        shape_name = "hexagon"

    elif corners == 7:
        shape_name = "heptagon"

    else:
        shape_name = "circle"

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
    x = approx.ravel()[0] # Multi dimensional array to 1D array
    y = approx.ravel()[1] - 10 # -10 to keep label above text
    cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 1)

cv2.imwrite("Contours.jpg", img)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()