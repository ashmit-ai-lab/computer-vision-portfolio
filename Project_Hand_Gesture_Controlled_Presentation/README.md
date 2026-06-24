# Hand Gesture Controlled Presentation

A computer vision project that allows you to control presentation slides and write on them using hand gestures in real-time.

Built using OpenCV and hand tracking, this system replaces traditional input devices (keyboard/mouse) with intuitive gestures.

---

## Features

- Right hand based gestures
- Slide navigation using hand gestures
- Draw annotations on slides using fingers
- Erase drawings with gesture
- Real-time hand tracking
- Smooth interaction with delay control (prevents accidental triggers)

---

## How It Works

1. Webcam captures live video
2. Hand is detected using a hand tracking module
3. Finger positions are analyzed
4. Gestures are mapped to actions:

| Gesture | Action |
|--------|--------|
| Index finger up | Draw |
| Thumb up | Previous slide |
| Little finger up | Next slide |
| Two fingers : index and middle up | Moving the draw pointer |
| Three fingers : Index, middle and ring up | Undo (Erase) |

---

## Project Structure

Project_Hand_Gesture_Controlled_Presentation/
│
├── Pres/ # Slides / images used in presentation
├── demo.avi # Demo video
├── main.py # Main application

---

## Tech Stack

- Python
- OpenCV
- cvzone (HandTrackingModule)
- NumPy

---

## Controls

- Keep hand above threshold line for gesture detection

- Use clear gestures for better accuracy

- Avoid fast/random movements


## How to Run
### 1. Install dependencies

```bash
pip install opencv-python cvzone numpy

### 2. Run the project
python main.py
