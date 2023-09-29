import mediapipe as mp
import cv2

def face_mesh(frame):
    face_mesh = mp.solutions.face_mesh.FaceMesh()

    while True:
        mesh_frame = frame.copy()

        cv2.resize(mesh_frame, (200, 200))
        results = face_mesh.process(mesh_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for landmark in face_landmarks.landmark:
                    x_coord, y_coord = [int(landmark.x * mesh_frame.shape[1]), int(landmark.y * mesh_frame.shape[0])]
                    cv2.circle(mesh_frame, (x_coord, y_coord), 1, (0, 255, 0), 2, 1)
        return mesh_frame

