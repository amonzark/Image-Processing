import cv2
from image_utils import display_image, save_image

def convert_image_color_to_grayscale(image):
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f"Grayscale shape: {gray.shape}")
        display_image(gray)
        save_image('save/grayscale.jpg', gray)
        return gray 
    else:
        print("Failed to load image for grayscale conversion.")
        return None

# --- Convert to RGB (from BGR) ---
def convert_image_color_to_rgb(image):
    if image is not None:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"RGB shape: {rgb.shape}")
        display_image(rgb)
        save_image('save/rgb.jpg', rgb)
        return rgb
    else:
        print("Failed to load image for RGB conversion.")
        return None

# --- Convert to HSV ---
def convert_image_color_to_hsv(image):
    if image is not None:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        print(f"HSV shape: {hsv.shape}")
        display_image(hsv)
        save_image('save/hsv.jpg', hsv)
        return hsv
    else:
        print("Failed to load image for HSV conversion.")
        return None

