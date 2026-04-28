import cv2
from image_utils import load_image, save_image

def convert_image_color_to_grayscale(image_path):
    image = load_image(image_path)
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f"Grayscale shape: {gray.shape}")  # (height, width) — no channel!
        #location = 'save/grayscale.jpg'
        #save_image(location, gray)
    else :
        print("Failed to load image for grayscale conversion.")

# --- Convert to RGB (from BGR) ---
def convert_image_color_to_rgb(image_path):
    image = load_image(image_path)
    if image is not None:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"RGB shape: {rgb.shape}")
        #location = 'save/rgb.jpg'
        #save_image(location, rgb)
    else:
        print("Failed to load image for RGB conversion.")

# --- Convert to HSV ---
# H = Hue (color), S = Saturation, V = Value (brightness)
def convert_image_color_to_hsv(image_path):
    image = load_image(image_path)
    if image is not None:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        print(f"HSV shape: {hsv.shape}")
        #location = 'save/hsv.jpg'
        #save_image(location, hsv)
    else:
        print("Failed to load image for HSV conversion.")