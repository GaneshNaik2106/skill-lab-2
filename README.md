# PROJECT-2 – Image Colorization on Raspberry Pi

This project downloads required models and then runs a Python script to colorize images using pre‑trained deep‑learning models on a Raspberry Pi.

---

## 1. Prerequisites

- Raspberry Pi (Raspberry Pi OS or any Linux‑based OS)  
- Internet connection  
- Python 3 and `pip` installed  
- Web browser (to access GitHub)

---

## 2. Setup Steps

### 1. Turn on Raspberry Pi and connect to internet  
- Power on the Raspberry Pi.  
- Connect it to Wi‑Fi or Ethernet so it has internet access.

### 2. Open the project repository  
- In a web browser, open:  
  ```text
  https://github.com/GaneshNaik2106/skill-lab-2
  ```

### 3. Download the ZIP  
- On the GitHub page, click the **Code** button.  
- Choose **Download ZIP** and save it to your Raspberry Pi.

### 4. Extract the ZIP file  
- Locate the downloaded ZIP (e.g., `skill-lab-2-main.zip`).  
- Extract it (e.g., **Extract Here** or via terminal: `unzip skill-lab-2-main.zip`).

### 5. Open the extracted folder  
- Navigate into the extracted folder (e.g., `skill-lab-2-main`).

### 6. Open a terminal in the project folder  
- Right‑click inside the folder and choose **Open Terminal Here** (or equivalent).  
- The terminal should be in the `skill-lab-2` project directory.

---

## 3. Python Virtual Environment & Dependencies

Run the following commands in the terminal:

### 7. Create a virtual environment  
```bash
python -m venv skill
```

This creates an isolated environment named `skill`.

### 8. Activate the virtual environment  
```bash
source ./skill/bin/activate
```

Your prompt should show `(skill)` at the beginning.

### 9. Install dependencies  
```bash
pip install -r requirements.txt
```

This installs all required packages listed in `requirements.txt`.

---

## 4. Download and Configure Models

### 10. Run the download script  
```bash
python download.py
```

This script downloads the model files (e.g., `.caffemodel`, `.prototxt`, `pts_in_hull.npy`, etc.) to a local folder such as `models/`.

### 11. Update model paths in colorize.py  
- Open `colorize.py` in a text editor:  
  ```bash
  nano colorize.py
  ```
- Look for variables that define model paths, for example:
  ```python
  proto_file = "path/to/colorization_deploy_v2.prototxt"
  model_file = "path/to/colorization_release_v2.caffemodel"
  hull_pts   = "path/to/pts_in_hull.npy"
  ```
- Update them to match the actual location of your downloaded models, such as:
  ```python
  proto_file = "models/colorization_deploy_v2.prototxt"
  model_file = "models/colorization_release_v2.caffemodel"
  hull_pts   = "models/pts_in_hull.npy"
  ```

Save and close the file.

### 12. Run the colorization script  
```bash
python colorize.py
```

The script will load the models, process the input image (either hardcoded or passed as an argument), and save or display the colorized output image.

---

## 5. Notes

- Ensure the `download.py` script successfully downloads all model files before running `colorize.py`.  
- If you restart the Pi, reactivate the environment with:  
  ```bash
  source ./skill/bin/activate
  ```  
  then run `python colorize.py` again.  
- If you want to colorize a different image, update the input image path in `colorize.py` similarly to the model paths.

---

## 6. License

Unless specified otherwise in the repository, treat this as an educational project and follow any license terms provided in the original `skill-lab-2` GitHub repository.
