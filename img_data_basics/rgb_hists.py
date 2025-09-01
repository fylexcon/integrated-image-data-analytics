from pathlib import Path
import cv2
import matplotlib.pyplot as plt


img_path = Path(__file__).parent / "data" / "images" / "example1.jpg"
img = cv2.cvtColor(cv2.imread(str(img_path)), cv2.COLOR_BGR2RGB)


output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)


plt.figure(figsize=(8,4))
for i, col in enumerate(["r", "g", "b"]):
    hist = cv2.calcHist([img], [i], None, [256], [0,256]).ravel()
    plt.plot(hist, label=col)
plt.title("RGB Histogramları")
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "rgb_hist.png", dpi=150)
plt.show()
