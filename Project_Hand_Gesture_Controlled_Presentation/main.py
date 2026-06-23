import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Variables
width, height = (1280, 720)
folder_path = "Pres"
imgnum = 0
hs, ws = int(120 * 1.4), int(231 * 1.2)
gestureThreshold = 370
butpressed = False
button_counter = 0
delay = 30 # Frames for which button should not do anything
annotations = [[]] #The inner list to remove the line between 2 disjoint points
annotationNumber = 0
annotationStart = False

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("demo.avi", codec, 30, (frame_width, frame_height))

# Get the list of presentation images
pathimg = sorted(os.listdir(folder_path), key = len) # to keep more than 10 images sorted

print(pathimg)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    succ, img = cap.read()
    #img = cv2.flip(img, 1)
    pathfullimg = os.path.join(folder_path, pathimg[imgnum])
    currimg = cv2.imread(pathfullimg)

    # Hand Tracking
    hands, img = detector.findHands(img, flipType=False)

    # Align the line with centre of face (if centre of hand above this line then only gesture accepted)
    #cv2.line(img,(0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)
            
    # Fingers
    if hands and butpressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmlist = hand['lmList']

        # Constrain values for easier drawing
        IndexFinger = lmlist[8][0], lmlist[8][1]
        xVal = int(np.interp(lmlist[8][0], [0, width//2], [width, 0]))
        yVal = int(np.interp(lmlist[8][1], [150, height - 150], [0, height]))
        IndexFinger = xVal, yVal
        
        if cy <= gestureThreshold:

            # Gesture 1 : Left
            if fingers == [1, 0, 0, 0, 0]:
                annotationStart = False
                if imgnum > 0:
                    butpressed = True
                    annotations = [[]]
                    annotationNumber = 0 
                    imgnum-=1

            # Gesture 2 : Right
            if fingers == [0, 0, 0, 0, 1]:
                annotationStart = False  
                if imgnum < len(pathimg) - 1:
                    butpressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgnum+=1

        # Gesture 3 : Show Pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(currimg, IndexFinger, 12, (0, 0, 255), cv2.FILLED)

        # Gesture 4 : Draw
        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(currimg, IndexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(IndexFinger)
        else :
            annotationStart = False

        # Gesture 5 : Eraser
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    annotationNumber-=1;
                    print(annotationNumber)
                    butpressed = True

    else :
        annotationStart = False
             
    # Button Pressed Iterations
    if butpressed:
        button_counter+=1
        if button_counter > delay:
            button_counter = 0
            butpressed = False
    
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j!=0:
                cv2.line(currimg, annotations[i][j-1], annotations[i][j], (0, 0, 255), 12)
            

    # Adding webcam image on the slide
    imgsmall = cv2.resize(img, (ws,hs))
    h, w, _ = currimg.shape
    currimg[0:hs, w-ws:w] = imgsmall

    cv2.imshow("Image", img)
    cv2.imshow("Slide", currimg)
    recorder.write(currimg)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

