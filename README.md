# ✨ MotionInk — Draw in the Air

**Turn your hand movements into digital art. No touchscreen. No physical canvas. Just your hand and a webcam.**

MotionInk is a real-time, gesture-controlled air drawing application built using Python, OpenCV and MediaPipe. It tracks hand movements through a webcam and translates fingertip movements into strokes on a virtual canvas.

The project explores the intersection of **Computer Vision, Hand Tracking and Human-Computer Interaction (HCI)** to create a more intuitive way of interacting with digital interfaces.

---

## 🎯 Features

- **Real-Time Hand Tracking:** Detects and tracks 21 hand landmarks using MediaPipe.
- **Air Drawing:** Draw on a virtual canvas using your index fingertip.
- **Gesture-Based Controls:** Interact with the canvas using intuitive hand gestures.
- **Colour Switching:** Change brush colours through hand gestures.
- **Pinch Interaction:** Use pinch gestures for interactive controls.
- **Eraser:** Remove unwanted strokes without restarting the application.
- **Neon Brush Effect:** Create glowing strokes for a more visually engaging drawing experience.
- **Live Webcam Feed:** View hand movements and drawing interactions in real time.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12.13 | Core programming language |
| OpenCV | Webcam processing and image manipulation |
| MediaPipe | Hand landmark detection and tracking |
| NumPy | Canvas and image array operations |
| Pygame CE | Graphics and visual effects |

---

## 🧠 How It Works

MotionInk follows a simple computer vision pipeline:

1. **Video Capture:** OpenCV captures frames from the webcam.
2. **Hand Detection:** MediaPipe identifies the hand and extracts 21 landmarks.
3. **Landmark Processing:** The application identifies relevant fingertips and interprets their positions.
4. **Gesture Recognition:** Hand configurations and movements are mapped to drawing commands.
5. **Canvas Rendering:** OpenCV and NumPy process and render the strokes.
6. **Visual Output:** The resulting drawing is displayed alongside the live camera feed.

### System Architecture

```text
          WEBCAM INPUT
               |
               v
       OPENCV VIDEO CAPTURE
               |
               v
      MEDIAPIPE HAND TRACKING
               |
               v
       21 HAND LANDMARKS
               |
               v
        GESTURE CONTROLLER
               |
        +------+------+
        |             |
        v             v
   DRAWING MODE   INTERACTION MODE
        |             |
        v             v
    CANVAS       COLOUR / ERASE
        |             |
        +------+------+
               |
               v
       RENDERED OUTPUT
```

---

## 📂 Project Structure

```text
03 MotionInk - Draw in the Air/
│
├── src/
│   ├── main.py
│   ├── hand_tracker.py
│   ├── drawing_canvas.py
│   └── gesture_controller.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Module Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Main application loop and integration |
| `hand_tracker.py` | Hand detection and landmark tracking |
| `drawing_canvas.py` | Drawing logic, strokes and visual effects |
| `gesture_controller.py` | Gesture interpretation and interaction |

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "03 MotionInk - Draw in the Air"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install mediapipe==0.10.21 opencv-contrib-python numpy pygame-ce
```

Alternatively:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python src/main.py
```

**Note:** Allow webcam access when prompted.

---

## 🎮 Controls

MotionInk uses hand gestures for drawing and interaction.

| Input | Action |
|---|---|
| Index finger | Draw |
| Index + middle finger | Stop drawing |
| Pinch gesture | Interactive colour control |
| Eraser gesture | Erase strokes |
| `C` | Clear canvas |
| `ESC` | Exit application |

---

## 🚀 What I Learned

Building MotionInk involved working with:

- Real-time computer vision pipelines.
- MediaPipe hand landmark detection.
- Coordinate tracking and gesture interpretation.
- Webcam frame processing using OpenCV.
- Virtual canvas manipulation using NumPy.
- Modular Python application architecture.
- Gesture-based human-computer interaction.

The interesting engineering challenge was translating continuous hand movements into stable digital interactions while keeping the experience responsive.

---

## 🔮 Future Improvements

- Add gesture customization.
- Introduce multiple brush styles and sizes.
- Implement drawing export and image saving.
- Improve gesture recognition accuracy.
- Explore multi-hand interaction.
- Optimize rendering performance and tracking latency.

---

## 👩‍💻 Author

**Sanchita Pawar**

Engineering Student | AI/ML & Computer Vision Enthusiast

Building projects at the intersection of technology, creativity and intelligent systems.


⭐ If you find this project interesting, consider giving the repository a star!

**MotionInk — Because your hands are already the perfect drawing tool.**
