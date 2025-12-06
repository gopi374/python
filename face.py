import cv2
import mediapipe as mp

def scan_body_parts():
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    landmark_names = mp_pose.PoseLandmark

    cap = cv2.VideoCapture(0)
    with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the BGR image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)

            # Draw pose landmarks on the image
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
                )
                h, w, _ = image.shape
                for idx, landmark in enumerate(results.pose_landmarks.landmark):
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    name = landmark_names(idx).name.replace("_", " ").title()
                    cv2.putText(image, name, (cx+5, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 0), 2)

            cv2.imshow('Body Part Scanner', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_body_parts()