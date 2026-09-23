import cv2
import numpy as np
import random
import time
from pathlib import Path

# =====================================
# GANPATI BAPPA - OPENCV LINE SKETCH
# =====================================

ROOT = Path(__file__).resolve().parent
IMAGE_PATH = ROOT / "ganesh.jpg"
OUTPUT_PATH = ROOT / "ganpati_red_outline.jpg"

WIDTH = 800
HEIGHT = 800
DELAY = 0.01


def create_red_outline_ganpati():
    canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    red = (0, 0, 255)
    cx, cy = WIDTH // 2, HEIGHT // 2 + 10

    # Outer circular frame
    cv2.circle(canvas, (cx, cy - 30), 330, red, 2)
    cv2.circle(canvas, (cx, cy - 30), 315, red, 1)

    # Crown/top ornament
    cv2.circle(canvas, (cx, cy - 200), 90, red, 2)
    cv2.ellipse(canvas, (cx, cy - 150), (110, 80), 0, 0, 180, red, 2)
    cv2.ellipse(canvas, (cx, cy - 230), (120, 60), 0, 180, 360, red, 2)

    # Head and ears
    cv2.ellipse(canvas, (cx, cy - 60), (165, 155), 0, 0, 360, red, 2)
    cv2.ellipse(canvas, (cx - 110, cy - 50), (40, 80), 0, 0, 360, red, 2)
    cv2.ellipse(canvas, (cx + 110, cy - 50), (40, 80), 0, 0, 360, red, 2)

    # Trunk and trunk highlight
    cv2.ellipse(canvas, (cx, cy + 10), (80, 120), 0, 0, 360, red, 2)
    cv2.ellipse(canvas, (cx, cy + 10), (30, 60), 0, 0, 360, red, 2)

    # Eyes and tusk
    cv2.circle(canvas, (cx - 42, cy - 65), 8, red, 2)
    cv2.circle(canvas, (cx + 42, cy - 65), 8, red, 2)
    cv2.ellipse(canvas, (cx, cy - 40), (18, 12), 0, 0, 180, red, 2)
    cv2.ellipse(canvas, (cx - 90, cy - 10), (35, 25), 0, 0, 180, red, 2)
    cv2.ellipse(canvas, (cx + 90, cy - 10), (35, 25), 0, 0, 180, red, 2)

    # Body / torso
    cv2.ellipse(canvas, (cx, cy + 150), (170, 150), 0, 0, 360, red, 2)
    cv2.ellipse(canvas, (cx, cy + 160), (115, 80), 0, 0, 360, red, 2)

    # Arms
    cv2.line(canvas, (cx - 150, cy + 60), (cx - 230, cy + 170), red, 3)
    cv2.line(canvas, (cx + 150, cy + 60), (cx + 230, cy + 170), red, 3)
    cv2.line(canvas, (cx - 230, cy + 170), (cx - 180, cy + 260), red, 3)
    cv2.line(canvas, (cx + 230, cy + 170), (cx + 180, cy + 260), red, 3)

    # Legs
    cv2.line(canvas, (cx - 80, cy + 300), (cx - 120, cy + 430), red, 3)
    cv2.line(canvas, (cx + 80, cy + 300), (cx + 120, cy + 430), red, 3)
    cv2.line(canvas, (cx - 120, cy + 430), (cx - 100, cy + 520), red, 3)
    cv2.line(canvas, (cx + 120, cy + 430), (cx + 100, cy + 520), red, 3)

    # Decorative curves
    cv2.ellipse(canvas, (cx - 160, cy + 220), (50, 60), 30, 0, 180, red, 2)
    cv2.ellipse(canvas, (cx + 160, cy + 220), (50, 60), -30, 0, 180, red, 2)
    cv2.ellipse(canvas, (cx - 120, cy + 360), (50, 40), 0, 0, 180, red, 2)
    cv2.ellipse(canvas, (cx + 120, cy + 360), (50, 40), 0, 0, 180, red, 2)

    # Base line decoration
    cv2.line(canvas, (cx - 160, cy + 520), (cx - 80, cy + 580), red, 3)
    cv2.line(canvas, (cx + 160, cy + 520), (cx + 80, cy + 580), red, 3)

    return canvas


def main():
    canvas = create_red_outline_ganpati()
    cv2.imwrite(str(OUTPUT_PATH), canvas)
    cv2.imshow("Ganpati Bappa Morya", canvas)
    print("Sketch Complete 🙏")
    print(f"Saved at: {OUTPUT_PATH}")
    print("Press any key to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
