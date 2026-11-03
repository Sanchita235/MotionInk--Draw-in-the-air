
try:
    import cv2  # type: ignore[reportMissingImports]
except ImportError as exc:
    raise ImportError(
        "OpenCV is required to run this project. Install it with: pip install opencv-python"
    ) from exc

import numpy as np


class DrawingCanvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.canvas = np.zeros(
            (height, width, 3),
            dtype=np.uint8
        )

        self.previous_point = None

        # OpenCV uses BGR colour order
        self.colors = {
            1: (255, 0, 255),    # Magenta
            2: (255, 100, 0),    # Blue
            3: (0, 255, 255),    # Yellow
            4: (0, 165, 255),    # Orange
            5: (0, 255, 0)       # Green
        }

        self.current_color = 1
        self.brush_size = 7
        self.eraser_size = 35

    def select_color(self, number):
        if number in self.colors:
            self.current_color = number

    def draw(self, point):
        if self.previous_point is not None:
            cv2.line(
                self.canvas,
                self.previous_point,
                point,
                self.colors[self.current_color],
                self.brush_size,
                cv2.LINE_AA
            )

        self.previous_point = point

    def erase(self, point):
        if self.previous_point is not None:
            cv2.line(
                self.canvas,
                self.previous_point,
                point,
                (0, 0, 0),
                self.eraser_size,
                cv2.LINE_AA
            )

        self.previous_point = point

    def stop_drawing(self):
        self.previous_point = None

    def clear(self):
        self.canvas[:] = 0
        self.previous_point = None

    def render(self, frame):

        # Generate glow from the drawing layer
        glow = cv2.GaussianBlur(
            self.canvas,
            (21, 21),
            0
        )

        # Combine camera, glow and original strokes
        output = cv2.addWeighted(
            frame, 1.0,
            glow, 0.9,
            0
        )

        output = cv2.addWeighted(
            output, 1.0,
            self.canvas, 1.0,
            0
        )

        return output
