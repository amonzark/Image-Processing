import cv2

def display_image(img):
    # Check input image before displaying
    if img is None or img.size == 0:
        print("Error: Image is None or empty!")
        return None
    
    print(f"Displaying image! Shape: {img.shape}")
    print(f"Data type: {img.dtype}")
    cv2.imshow('Image', img)
    return img

def save_image(path, img):
    save = cv2.imwrite(path, img)
    if save:
        print(f"Image saved at {path}")
    else:
        print(f"Error: Failed to save image at {path}")
