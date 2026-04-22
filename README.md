# Black & White Image Colorization

A Python application that automatically colorizes black and white images using a pre-trained deep learning model based on Caffe framework.

## Features

- Converts grayscale/black & white images to color automatically
- Uses advanced deep learning (Zhang et al. 2016 colorization model)
- Fast processing with OpenCV's DNN module
- Supports common image formats (JPEG, PNG, etc.)

## Requirements

- Python 3.6+
- OpenCV (`opencv-python==4.13.0.92`)
- NumPy (`numpy==2.0.2`)

## Installation

1. **Download the project:**
   - Go to [GitHub Repository](https://github.com/GaneshNaik2106/skill-lab-2)
   - Click the green **Code** button
   - Select **Download ZIP**
   - Extract the ZIP file to your desired location

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Pre-trained Models

The following pre-trained Caffe models are included in the downloaded project:

- `colorization_deploy_v2.prototxt` - Model architecture
- `colorization_release_v2.caffemodel` - Pre-trained weights
- `pts_in_hull.npy` - Color cluster centers

## Usage

1. Place your black & white image in the project folder and name it `blacknwhite.jpeg` 
   (or update the `IMAGE_PATH` variable in the script)

2. Run the colorization script:
```bash
python colorize.py
```

3. The colorized image will be saved as `colorized_output.jpg` 
   (or the path specified in `OUTPUT_PATH`)

### Customization

Edit `colorize.py` to change:
- `IMAGE_PATH`: Input image file path
- `OUTPUT_PATH`: Output image file path
- Model paths if you organize files differently

## How It Works

1. **Model Loading**: Loads the pre-trained Caffe colorization model
2. **Preprocessing**: Converts image to LAB color space and resizes to 224x224
3. **Prediction**: Uses neural network to predict color information (ab channels)
4. **Postprocessing**: Resizes predictions back to original dimensions and converts to BGR
5. **Output**: Saves the colorized image

