<div align="center">

```
██╗███╗   ███╗ █████╗  ██████╗ ███████╗    ██████╗ ██████╗  ██████╗  ██████╗
██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║██╔████╔██║███████║██║  ███╗█████╗      ██████╔╝██████╔╝██║   ██║██║
██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██╔═══╝ ██╔══██╗██║   ██║██║
██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ██║     ██║  ██║╚██████╔╝╚██████╗
╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝
```

# 🖼️ Image Processing with Python & OpenCV

**See the world in grayscale. In RGB. In HSV. See it differently.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning%20in%20Progress-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

</div>

---

## 🌈 What Is This?

Ever wondered **what a computer actually sees** when it looks at a photo?

This project is a hands-on journey into **image processing** — the foundational skill behind everything from Instagram filters to medical imaging to self-driving cars. Using Python and OpenCV, we load, transform, and save images across different color spaces to understand how digital images are really represented under the hood.

> *"An image is just a matrix of numbers — until you learn to speak its language."*

---

## ✨ Features at a Glance

| 🔧 Feature | 📝 Description |
|---|---|
| 📂 **Load & Validate** | Load any image with error handling — no silent crashes |
| 🌑 **Grayscale Conversion** | Strip away color, keep the structure |
| 🔴 **BGR → RGB** | Flip the channel order the way the human eye prefers |
| 🌈 **HSV Conversion** | Separate Hue, Saturation, Value — perfect for color detection |
| 💾 **Auto-Save** | All processed outputs saved automatically to `/save` |

---

## 📁 Project Structure

```
Image-Processing/
│
├── 📄 main.py            # Entry point — runs all transformations
├── 🛠️  image_utils.py    # Reusable helper functions (load & save)
├── 🖼️  images.jpg        # Sample input image
│
└── 📁 save/              # Output directory
    ├── output.jpg        # Original copy
    ├── grayscale.jpg     # Grayscale version
    ├── rgb.jpg           # RGB version
    └── hsv.jpg           # HSV version
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/amonzark/Image-Processing.git
cd Image-Processing
```

### 2. Install dependencies

```bash
pip install opencv-python
```

### 3. Run it!

```bash
python main.py
```

That's it. Four windows will pop up, each showing the same image through a different lens. ✅

---

## 🧠 How It Works

### `image_utils.py` — The Utility Belt

```python
def load_image(path):
    img = cv2.imread(path)
    # Validates the image and prints its shape + dtype
    return img

def save_image(path, img):
    # Saves to disk and confirms success or failure
    cv2.imwrite(path, img)
```

Two clean, reusable functions. Load with validation. Save with confirmation. No guesswork.

---

### `main.py` — The Pipeline

```python
# Step 1 — Load
img = load_image('images.jpg')

# Step 2 — Show & Save Original
cv2.imshow('Image', img)
save_image('save/output.jpg', img)

# Step 3 — Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4 — RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 5 — HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

A clean linear pipeline: **load → transform → display → save**. Simple, readable, educational.

---

## 🎨 Color Space Deep Dive

Understanding *why* we convert between color spaces is the real lesson here:

### 🌑 Grayscale
Reduces a 3-channel image to 1 channel. Great for edge detection, thresholding, and reducing computation. The formula isn't just averaging — OpenCV uses perceptual weighting so brighter colors appear brighter to the human eye.

### 🔴 RGB (from BGR)
OpenCV loads images as BGR by default (Blue-Green-Red), which is the opposite of what most humans expect. Converting to RGB makes the colors display correctly in matplotlib and other tools.

### 🌈 HSV (Hue-Saturation-Value)
The most powerful space for color-based detection. Want to isolate "all the red objects in this image"? HSV makes it trivially easy. Hue captures the *color*, Saturation captures *intensity*, Value captures *brightness*.

---

## 📦 Requirements

```
Python >= 3.7
opencv-python >= 4.0
```

---

## 🗺️ Roadmap

What's coming next as this learning journey continues:

- [ ] 🔲 Edge Detection (Canny, Sobel)
- [ ] 🌫️ Image Blurring & Noise Reduction
- [ ] 📐 Image Resizing & Cropping
- [ ] 🎭 Thresholding & Masking
- [ ] 🔍 Object Detection basics
- [ ] 🧩 Histogram Equalization

---

## 🙋 About This Repo

This is a **personal learning repository** focused on building image processing skills from the ground up. The goal is to understand the fundamentals before jumping to deep learning — because knowing how pixels work makes you a better computer vision engineer.

Built with curiosity. Documented for anyone who's starting the same journey. 🚀

---

<div align="center">

**If this helped you, drop a ⭐ — it means a lot!**

Made with ❤️ and `cv2` by [amonzark](https://github.com/amonzark)

</div>
