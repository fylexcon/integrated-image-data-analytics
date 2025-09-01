from pathlib import Path
import cv2
import pandas as pd


img_path = Path(__file__).parent / "data" / "images" / "example1.jpg"
img = cv2.cvtColor(cv2.imread(str(img_path)), cv2.COLOR_BGR2RGB)

r = img[:,:,0].reshape(-1)
g = img[:,:,1].reshape(-1)
b = img[:,:,2].reshape(-1)

df = pd.DataFrame({"R": r, "G": g, "B": b})
stats = df.describe()


output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)
stats.to_csv(output_dir / "rgb_stats.csv", index=True)

print(stats)
