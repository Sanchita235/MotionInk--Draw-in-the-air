
import cv2  # type: ignore
import mediapipe as mp  # type: ignore


class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def detect_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        landmarks = None

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]

            self.mp_draw.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand.landmark

        return frame, landmarks

    def close(self):
        self.hands.close()
