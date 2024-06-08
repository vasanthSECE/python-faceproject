import cv2

def count_faces_from_camera():
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

   
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream from camera.")
        return

    while True:
       
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break

       
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

       
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        
        cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        
        cv2.imshow('Face Detection', frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

   
    cap.release()
    cv2.destroyAllWindows()


count_faces_from_camera()
