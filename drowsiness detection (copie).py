import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from mtcnn.mtcnn import MTCNN
import pygame

# Initialisation de pygame pour l'alarme
pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')  # Assurez-vous que le chemin est correct

# Initialisation des détecteurs
mtcnn_detector = MTCNN()
dlib_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
dlib_detector = dlib.get_frontal_face_detector()

video_capture = cv2.VideoCapture(0)

# Seuils
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 20
COUNTER = 0

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Utiliser MTCNN pour la détection des visages
    faces = mtcnn_detector.detect_faces(frame)
    if faces:
        for face in faces:
            bounding_box = face['box']
            keypoints = face['keypoints']

            # Dessiner un rectangle autour du visage détecté
            cv2.rectangle(frame, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1]+bounding_box[3]), (0, 155, 255), 2)

            # Conversion du rectangle de MTCNN pour dlib
            dlib_rect = dlib.rectangle(left=bounding_box[0], top=bounding_box[1], right=bounding_box[0]+bounding_box[2], bottom=bounding_box[1]+bounding_box[3])

            # Utiliser dlib pour obtenir les points de repère faciaux
            shape = dlib_predictor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), dlib_rect)
            shape_np = np.array([(p.x, p.y) for p in shape.parts()])

            leftEye = shape_np[42:48]
            rightEye = shape_np[36:42]

            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0

            if ear < EYE_AR_THRESH:
                COUNTER += 1
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()
                COUNTER = 0

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
