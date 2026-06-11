# 🎓 AI Proctoring System

A real-time AI-powered proctoring system built using **Python, OpenCV, and MediaPipe**. The application monitors candidates during online examinations by detecting faces through a webcam and generating alerts for suspicious situations such as multiple faces or absence of a candidate.

---

## 🚀 Features

* Real-time webcam monitoring
* Face detection using MediaPipe
* Candidate verification
* Multiple face detection alert
* No face detected alert
* Live face count display
* Lightweight and fast execution

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* Computer Vision

---

## 📂 Project Structure

```text
AI_Proctoring_System/
│
├── main.py
├── README.md
│
└── screenshots/
    ├── candidate_verified.png
    ├── no_face_alert.png
    └── multiple_faces_alert.png
```

---

## 📸 Screenshots

### Candidate Verified

<img width="645" height="511" alt="Screenshot 2026-06-11 193052" src="https://github.com/user-attachments/assets/a0ebbd32-be74-41ef-a0f5-0ebf46cbc7a0" />


### No Face Detected Alert

<img width="630" height="513" alt="Screenshot 2026-06-11 193117" src="https://github.com/user-attachments/assets/794a9cb7-9557-43cd-a4ed-80a640929a0a" />


### Multiple Faces Detected Alert

<img width="514" height="313" alt="Screenshot 2026-06-11 194314" src="https://github.com/user-attachments/assets/09234e1c-ed21-4db0-9e9a-d6e8319f0681" />


---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI_Proctoring_System.git
```

### Navigate to Project Folder

```bash
cd AI_Proctoring_System
```

### Install Dependencies

```bash
pip install opencv-python mediapipe
```

### Run the Application

```bash
python main.py
```

---

## 🧠 How It Works

1. Captures live webcam feed.
2. Detects faces using MediaPipe Face Detection.
3. Counts the number of faces present.
4. Displays:

   * Candidate Verified
   * No Face Detected Alert
   * Multiple Faces Detected Alert
5. Updates status in real time.

---

## 📊 Sample Output

### Single Face

```text
Candidate Verified
Faces: 1
```

### No Face Present

```text
ALERT: NO FACE DETECTED
Faces: 0
```

### Multiple Faces Present

```text
ALERT: MULTIPLE FACES
Faces: 2
```

---

## 🎯 Applications

* Online Examination Monitoring
* Remote Assessments
* Educational Platforms
* Recruitment Tests
* Interview Monitoring Systems

---

## 🔮 Future Enhancements

* Eye Gaze Tracking
* Head Pose Estimation
* Looking Away Detection
* Mobile Phone Detection
* Person Identification
* Exam Violation Logging
* Report Generation Dashboard
* YOLO-Based Object Detection Integration

---

## 📈 Learning Outcomes

* Face Detection using MediaPipe
* Real-Time Video Processing
* OpenCV Applications
* Human Monitoring Systems
* Computer Vision Fundamentals

---

## 👩‍💻 Author

**Shreya Gaur**

Machine Learning • Computer Vision • Generative AI

---

⭐ If you found this project useful, consider giving the repository a star.
