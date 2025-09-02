from pathlib import Path
import cv2
import pandas as pd
from glob import glob


img_dir = Path(__file__).parent / "data" / "images"


output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

rows = []


for fp in glob(str(img_dir / "*.jpg")):
    img_bgr = cv2.imread(fp)
    if img_bgr is None:
        print(f"Warning: {fp} okunamadı, atlanıyor.")
        continue
    img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    r, g, b = img[:,:,0].ravel(), img[:,:,1].ravel(), img[:,:,2].ravel()
    
    rows.append({
        "file": Path(fp).name,
        "mean_R": r.mean(),
        "mean_G": g.mean(),
        "mean_B": b.mean(),
        "std_R": r.std(),
        "std_G": g.std(),
        "std_B": b.std(),
        "pixels": r.size
    })

summary = pd.DataFrame(rows).sort_values("file")
summary.to_csv(output_dir / "multi_image_summary.csv", index=False)

print("Multi-image summary:")
print(summary)
