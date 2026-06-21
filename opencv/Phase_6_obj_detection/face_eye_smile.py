import cv2

face_cascade = cv2.CascadeClassifier(r"..\assets\haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier(r"..\assets\haarcascade_eye_tree_eyeglasses.xml") 
smile_cascade = cv2.CascadeClassifier(r"..\assets\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.avi", codec, 30, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 7) # zoom in frames and number of tests

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0, 255, 0), thickness=2)

        # Region of face (taking out face only for eye and smile) (roi = region of interest)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

        if len(eyes) > 0:
            cv2.putText(frame, "Eyes detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (10,255,0), 1)

        smile = smile_cascade.detectMultiScale(roi_gray, 1.2, 13)
        if len(smile) > 0:
            cv2.putText(frame, "Smiling", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (10,255,0), 1)

    recorder.write(frame)
    cv2.imshow("Smart face detector", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()
