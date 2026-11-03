
import math


class GestureController:

    def get_gesture(self, landmarks):
        # Get thumb and index fingertip coordinates
        thumb = landmarks[4]
        index = landmarks[8]

        # Calculate distance between fingertips
        pinch_distance = math.hypot(
            thumb.x - index.x,
            thumb.y - index.y
        )

        # Normalise pinch distance using palm size
        wrist = landmarks[0]
        middle_base = landmarks[9]

        palm_size = math.hypot(
            wrist.x - middle_base.x,
            wrist.y - middle_base.y
        )

        if palm_size == 0:
            return "IDLE"

        normalized_pinch = pinch_distance / palm_size

        # Pinch gesture activates eraser
        if normalized_pinch < 0.35:
            return "ERASE"

        # Check index and middle fingers
        index_up = landmarks[8].y < landmarks[6].y
        middle_up = landmarks[12].y < landmarks[10].y

        if index_up and not middle_up:
            return "DRAW"

        if index_up and middle_up:
            return "STOP"

        return "IDLE"
