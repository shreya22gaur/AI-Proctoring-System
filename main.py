import cv2
import mediapipe as mp

# MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection

face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = face_detection.process(rgb)

    face_count = 0

    if results.detections:
        face_count = len(results.detections)

    # Rule 1: No Face
    if face_count == 0:

        cv2.putText(
            frame,
            "ALERT: NO FACE DETECTED",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Rule 2: Multiple Faces
    elif face_count > 1:

        cv2.putText(
            frame,
            "ALERT: MULTIPLE FACES",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Rule 3: Normal
    else:

        cv2.putText(
            frame,
            "Candidate Verified",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Faces: {face_count}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "AI Proctoring System",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()