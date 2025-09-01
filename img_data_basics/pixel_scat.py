from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt


img_path = Path(__file__).parent / "data" / "images" / "example1.jpg"
img = cv2.cvtColor(cv2.imread(str(img_path)), cv2.COLOR_BGR2RGB)

H, W, _ = img.shape
r = img[:,:,0].reshape(-1)
g = img[:,:,1].reshape(-1)
b = img[:,:,2].reshape(-1)


n = min(50000, r.size)
idx = np.random.choice(r.size, n, replace=False)
rc, gc, bc = r[idx], g[idx], b[idx]


plt.figure(figsize=(6,6))
plt.scatter(rc, gc, c=np.stack([rc, gc, bc], 1)/255.0, s=1, alpha=0.6)
plt.xlabel("Red")
plt.ylabel("Green")
plt.title("Piksel Dağılımı (R vs G)")
plt.tight_layout()


output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)
plt.savefig(output_dir / "rg_scatter.png", dpi=150)
plt.show()
