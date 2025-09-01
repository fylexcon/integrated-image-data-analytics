from pathlib import Path
import cv2
import matplotlib.pyplot as plt

img_path = Path(__file__).parent / "data" / "images" / "example1.jpg"


img_bgr = cv2.imread(str(img_path))
if img_bgr is None:
    raise FileNotFoundError(f"Image not found at {img_path}")


img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
print("Image loaded:",img.shape)
