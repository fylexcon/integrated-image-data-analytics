import subprocess
import sys

scripts = [
    "read_img.py",
    "rgb_hists.py",
    "pixel_scat.py",
    "rgb_stats.py",
    "multi_img_summary.py"
]

for script in scripts:
    print(f"\n--- : {script} ---")
    subprocess.run([sys.executable, f"img_data_basics/{script}"])
