import os
import face_recognition
import cv2
import numpy as np



known_encodings = []
known_names = []

for filename in os.listdir("knowns"):
    path = os.path.join("knowns", filename)
    img = face_recognition.load_image_file(path)
    encodings = face_recognition.face_encodings(img)
    if encodings:
        known_encodings.append(encodings[0])
        known_names.append(os.path.splitext(filename)[0]) 


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

   
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "UNKNOWN"

        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)

        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

      
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255), 2)
        cv2.putText(frame, name, (left, bottom + 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
