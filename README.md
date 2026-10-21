# Hand Mouse Control

Control your computer's mouse cursor with hand gestures using a webcam. The program tracks your hand with MediaPipe, moves the cursor with your index finger, and clicks when you pinch your thumb and index finger together.

## Features

- Real-time hand tracking from a standard webcam
- Cursor movement that follows the tip of your index finger
- Click gesture: pinch the thumb and index finger together
- Click cooldown (0.5 seconds) to prevent accidental double clicks
- Live preview window with hand landmarks drawn on the video

## How it works

1. OpenCV captures frames from the webcam and mirrors them.
2. MediaPipe Hands detects one hand and returns 21 landmarks.
3. The index fingertip (landmark 8) position is mapped to screen coordinates, and PyAutoGUI moves the cursor there.
4. The distance between the index fingertip (landmark 8) and the thumb tip (landmark 4) is measured. When it falls below 30 pixels, a click is sent.

## Requirements

- A webcam
- A Python version supported by MediaPipe
- Packages listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/<your-username>/hand-mouse-control.git
cd hand-mouse-control
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python hand_mouse.py
```

| Action | Gesture or key |
|--------|----------------|
| Move the cursor | Move your index finger in front of the camera |
| Click | Pinch your thumb and index finger together |
| Quit | Press `Q` while the preview window is focused |

## Tips

- Use good, even lighting and a plain background for better tracking.
- Keep your hand fully visible and at a moderate distance from the camera.
- Close other applications that may be using the camera.
- If the cursor does not respond, make sure the preview window is running and your hand is detected.

## Safety notes

- The program takes control of your real mouse. Keep the preview window available so you can press `Q` to stop it.
- PyAutoGUI's fail-safe is active by default: moving the cursor into a screen corner raises an exception and stops the program.

## Limitations

- Only one hand is tracked.
- The click threshold is a fixed pixel distance, so it depends on how far your hand is from the camera.
- There is no cursor smoothing, so movement can look slightly jittery.
- Right click, scrolling, and drag gestures are not implemented.

## Possible improvements

- Smooth cursor movement with a moving average
- Click threshold relative to hand size
- Right click, scroll, and drag gestures
- A margin area so the edges of the screen are easier to reach

## License

MIT License. See the `LICENSE` file.
