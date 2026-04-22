import os
import urllib.request

# ============================
# Create models directory
# ============================
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# ============================
# Model URLs
# ============================
urls = {
    "colorization_deploy_v2.prototxt":
        "https://raw.githubusercontent.com/richzhang/colorization/caffe/colorization/models/colorization_deploy_v2.prototxt",

    "pts_in_hull.npy":
        "https://raw.githubusercontent.com/richzhang/colorization/caffe/colorization/resources/pts_in_hull.npy",

    "colorization_release_v2.caffemodel":
        "https://huggingface.co/spaces/BilalSardar/Black-N-White-To-Color/resolve/main/colorization_release_v2.caffemodel"
}

# ============================
# Download function
# ============================
def download_file(url, filepath):
    try:
        print(f"\n⬇️ Downloading: {os.path.basename(filepath)}")

        def progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = downloaded / total_size * 100 if total_size > 0 else 0
            print(f"\rProgress: {percent:.2f}%", end="")

        urllib.request.urlretrieve(url, filepath, progress)

        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"\n✅ Done: {os.path.basename(filepath)} ({size_mb:.2f} MB)")

    except Exception as e:
        print(f"\n❌ Failed: {os.path.basename(filepath)}")
        print("Error:", e)

# ============================
# Download all models
# ============================
print("🚀 Starting model downloads...")

for name, url in urls.items():
    filepath = os.path.join(MODEL_DIR, name)

    # Skip if already exists
    if os.path.exists(filepath):
        print(f"✔ Already exists: {name}")
        continue

    download_file(url, filepath)

print("\n🎉 All downloads completed!")