import cv2

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        print("Error: Image not found!")
    else:
        print(f"Image loaded! Shape: {img.shape}")
        print(f"Data type: {img.dtype}")
    return img

def save_image(path, img):
    save = cv2.imwrite(path, img)
    if save:
        print(f"Image saved at {path}")
    else:
        print(f"Error: Failed to save image at {path}")