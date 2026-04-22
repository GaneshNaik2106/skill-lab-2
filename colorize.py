# ================================================
# Black & White Image Colorization - Raspberry Pi
# ================================================

import cv2
import numpy as np
import os

# ============================
# 1. Paths (keep models in ./models/)
# ============================
PROTO = r"models\colorization_deploy_v2.prototxt"
MODEL = r"models\colorization_release_v2.caffemodel"
POINTS = r"models\pts_in_hull.npy"

IMAGE_PATH = "blacknwhite.jpeg"   # your B&W image
OUTPUT_PATH = "colorized_output.jpg"

# ============================
# 2. Load Model
# ============================
print("Loading model...")

net = cv2.dnn.readNetFromCaffe(PROTO, MODEL)
pts = np.load(POINTS)

# Add cluster centers
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")

pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

print("Model loaded successfully!")

# ============================
# 3. Read Image
# ============================
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image not found!")
    exit()

print("Colorizing...")

# ============================
# 4. Preprocess
# ============================
scaled = img.astype("float32") / 255.0
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

resized = cv2.resize(lab, (224, 224))
L = cv2.split(resized)[0]
L -= 50

# ============================
# 5. Predict
# ============================
net.setInput(cv2.dnn.blobFromImage(L))
ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

# ============================
# 6. Postprocess
# ============================
ab = cv2.resize(ab, (img.shape[1], img.shape[0]))
L = cv2.split(lab)[0]

colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)

colorized = np.clip(colorized, 0, 1)
colorized = (255 * colorized).astype("uint8")

# ============================
# 7. Save Output
# ============================
cv2.imwrite(OUTPUT_PATH, colorized)

print(f"Done! Saved as {OUTPUT_PATH}")