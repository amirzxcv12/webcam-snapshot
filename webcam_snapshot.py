from pathlib import Path
from datetime import datetime

import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise SystemExit("Could not open the webcam.")

# Keep captured images in one folder beside this script.
output_dir = Path(__file__).parent / "captures"
output_dir.mkdir(exist_ok=True)

print("Press SPACE to take a photo. Press Q to quit.")

while True:
    success, frame = camera.read()
    if not success:
        print("Could not read a frame.")
        break

    frame = cv2.flip(frame, 1)

    # Show simple instructions on the camera preview.
    cv2.putText(
        frame, "SPACE: Take photo | Q: Quit", (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2
    )

    cv2.imshow("Webcam Snapshot", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord(" "):
        # Use the current time to avoid overwriting earlier photos.
        filename = datetime.now().strftime("photo_%Y%m%d_%H%M%S_%f.jpg")
        photo_path = output_dir / filename

        if cv2.imwrite(str(photo_path), frame):
            print(f"Saved: {photo_path}")
        else:
            print("Could not save the photo.")

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
