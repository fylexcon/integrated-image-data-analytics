import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

img_path = Path(__file__).parent / "data" / "images" / "example1.jpg"

img_bgr = cv2.imread(str(img_path))
if img_bgr is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)  # Fix: use BGR for grayscale conversion

blur_gauss = cv2.GaussianBlur(gray, (5, 5), 0)
blur_median = cv2.medianBlur(gray, 5)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
sobel_msg = cv2.magnitude(sobelx, sobely)

edges_canny = cv2.Canny(gray, 100, 200)

laplacian = cv2.Laplacian(blur_gauss, cv2.CV_64F)

_, thresh = cv2.threshold(blur_gauss, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_contours = img_rgb.copy()
cv2.drawContours(img_contours, contours, -1, (255, 0, 0), 2)

print(f"Contour count: {len(contours)}")

output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Gray Image")

plt.subplot(1, 2, 2)
plt.imshow(img_contours)
plt.title(f"Contours ({len(contours)} found)")

plt.tight_layout()
plt.savefig(output_dir / "edges_and_contours.png")
plt.show()