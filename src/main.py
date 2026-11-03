
try:
    import cv2  # type: ignore[import-not-found]
except ModuleNotFoundError:
    cv2 = None

from hand_tracker import HandTracker
from drawing_canvas import DrawingCanvas
from gesture_controller import GestureController


WIDTH = 1280
HEIGHT = 720


def main():
    if cv2 is None:
        print("ERROR: OpenCV is not installed. Install it with: pip install opencv-python")
        return

    camera = cv2.VideoCapture(0)

    tracker = HandTracker()
    controller = GestureController()
    canvas = DrawingCanvas(WIDTH, HEIGHT)

    if not camera.isOpened():
        print("ERROR: Webcam could not open.")
        tracker.close()
        return

    print("\n========== MOTIONINK ==========")
    print("Index finger       : Draw")
    print("Index + middle     : Stop")
    print("Thumb + index pinch: Erase")
    print("Keys 1-5           : Change colour")
    print("C                  : Clear canvas")
    print("ESC                : Exit")
    print("===============================\n")

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (WIDTH, HEIGHT))

        frame, landmarks = tracker.detect_hands(frame)

        gesture = "NO HAND"

        if landmarks:

            index_tip = landmarks[8]

            x = int(index_tip.x * WIDTH)
            y = int(index_tip.y * HEIGHT)

            point = (x, y)

            gesture = controller.get_gesture(landmarks)

            if gesture == "DRAW":
                canvas.draw(point)
                cv2.circle(frame, point, 9, (0, 255, 0), -1)

            elif gesture == "ERASE":
                canvas.erase(point)
                cv2.circle(frame, point, 15, (255, 255, 255), 2)

            else:
                canvas.stop_drawing()

        else:
            canvas.stop_drawing()

        output = canvas.render(frame)

        # Display gesture and selected colour
        cv2.putText(
            output,
            f"Gesture: {gesture}",
            (25, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.putText(
            output,
            f"Colour: {canvas.current_color}",
            (25, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            output,
            "1-5: Colours | C: Clear | ESC: Exit",
            (25, HEIGHT - 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.imshow("MotionInk - Neon Air Drawing", output)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

        elif key == ord("c"):
            canvas.clear()

        elif key in [ord(str(i)) for i in range(1, 6)]:
            canvas.select_color(int(chr(key)))

    camera.release()
    tracker.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
