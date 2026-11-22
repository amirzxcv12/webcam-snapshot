# Webcam Snapshot

A tiny webcam camera app that saves photos to your computer.

## Features
- Live camera preview
- Mirror-style view
- Save a photo with the space bar
- Automatic `captures` folder
- Timestamped image filenames

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# On Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python webcam_snapshot.py
```

## Controls

- **Space** — save the current frame
- **Q** — quit

Photos are saved in the `captures/` folder next to the Python script.

## Project structure

```text
webcam-snapshot/
├── webcam_snapshot.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Creator
**Amir**

Made with Python and OpenCV 💜
