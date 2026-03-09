😊 Emotion Detection System

A Python-based Emotion Detection System that identifies human emotions from facial expressions using Computer Vision and Deep Learning.

This project includes two main parts:

🧠 Training using emotion images

🎥 Real-time emotion detection using webcam

The system uses OpenCV for image processing and the FER (Facial Emotion Recognition) library with MTCNN for accurate face detection and emotion prediction.

📂 Project Structure
Emotion-Detection
│
├── emotion recognition source code.py      # Main program (Live emotion detection)
├── emotion recognition image code.py       # Training using emotion images
├── requirements.txt
├── README.md
├── LICENSE
│
└── Emotions
    ├── Happy
    ├── Surprise
    ├── Fear
    ├── Sad
    └── Angry
🚀 Features

✅ Real-time emotion detection using webcam
✅ Emotion analysis from training images
✅ Detects multiple faces
✅ Displays emotion with confidence percentage
✅ Automatically creates emotion folders
✅ Uses MTCNN for better face detection

🧠 Emotions Detected

The system detects the following emotions:

😄 Happy

😲 Surprise

😨 Fear

😢 Sad

😡 Angry

⚠️ Neutral emotion is ignored.

🛠️ Installation
1️⃣ Clone the repository
git clone https://github.com/rsamwilson2323-cloud/Emotion-Detection.git
cd Emotion-Detection
2️⃣ Install dependencies
pip install -r requirements.txt
▶️ Usage
🧠 Step 1 — Training Using Images

Run the image training script:

python emotion recognition image code.py

Add images inside the Emotions folder according to emotion category:

Emotions/
Happy/
Sad/
Angry/
Fear/
Surprise/

The program will analyze images and print detected emotions.

🎥 Step 2 — Real-Time Emotion Detection

Run the main program:

python emotion recognition source code.py

📷 The webcam will start automatically.

Press ENTER to close the camera window.

📦 Requirements

Main libraries used:

Python

OpenCV

FER

TensorFlow

MTCNN

Install them using:

pip install -r requirements.txt
👨‍💻 Author

Sam Wilson

🔗 https://github.com/rsamwilson2323-cloud

💼 https://www.linkedin.com/in/sam-wilson-14b554385
