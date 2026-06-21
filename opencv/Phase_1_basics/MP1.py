import cv2

path = input("Enter image path : ")

image = cv2.imread(path, 1)

print("What do you want to do with the image ?")

while True :
    choice = int(input("1. Show\n2. Save\n3. Exit\n"))

    if choice == 1:
        cv2.imshow("Love", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 2:
        n = input("Enter saving name : ")
        cv2.imwrite(n + ".jpg", image)
        print(n + " Saved successfully.")
    else: 
        break
