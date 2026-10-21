import cv2
import mediapipe as mp
import pyautogui
import time

# Screen size
screen_width, screen_height = pyautogui.size()

# Mediapipe hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_click_time = 0
click_cooldown = 0.5  # seconds, to avoid multiple accidental clicks

while True:
    success, frame = cap.read()
    if not success:
        print("Could not open the camera. Check that no other application is using it.")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Index finger tip = landmark 8, Thumb tip = landmark 4
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # Convert to pixel coords
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # Move mouse based on index finger position
            screen_x = int(index_tip.x * screen_width)
            screen_y = int(index_tip.y * screen_height)
            pyautogui.moveTo(screen_x, screen_y, duration=0.01)

            # Distance between thumb and index finger tip -> click gesture
            distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5

            if distance < 30:
                current_time = time.time()
                if current_time - prev_click_time > click_cooldown:
                    pyautogui.click()
                    prev_click_time = current_time
                    cv2.putText(frame, "Click!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Mouse Control - press Q to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()