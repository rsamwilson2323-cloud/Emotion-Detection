import os
import sys
import warnings

# Hide TensorFlow logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull, "w")

import cv2
from fer import FER

# Initialize emotion detector
detector = FER(mtcnn=True)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open webcam")
    sys.exit()

print("🎥 Camera started — press ENTER to exit\n")

while True:

    ret, frame = cap.read()
    if not ret:
        continue

    # Detect emotions
    try:
        results = detector.detect_emotions(frame)
    except:
        results = []

    # Number of people detected
    people_count = len(results)

    cv2.putText(
        frame,
        f"People: {people_count}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,255),
        2
    )

    for face in results:

        x, y, w, h = face["box"]

        emotions = face["emotions"]

        # Remove neutral emotion
        emotions.pop("neutral", None)

        if emotions:

            top_emotion = max(emotions, key=emotions.get)
            confidence = emotions[top_emotion] * 100

            label = f"{top_emotion.capitalize()} {confidence:.1f}%"

            # Draw face box
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            # Background for text
            cv2.rectangle(frame,(x,y-30),(x+w,y),(255,0,0),-1)

            # Emotion text
            cv2.putText(
                frame,
                label,
                (x+5,y-8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2,
                cv2.LINE_AA
            )

    # Show window
    cv2.imshow("Emotion Detection", frame)

    # Press ENTER to exit
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

print("\n✅ Camera closed")

