import cv2

def crop_image(image, x_start, x_end, y_start, y_end):
    if image is not None:
        cropped = image[y_start:y_end, x_start:x_end]
        print(f"Cropped shape: {cropped.shape}")
        return cropped
    else:
        print("Failed to load image for cropping.")
        return None

def resize_image(image, new_width, new_height):
    if image is not None:
        resized = cv2.resize(image, (new_width, new_height))
        print(f"Resized shape: {resized.shape}")
        return resized
    else:
        print("Failed to load image for resizing.")
        return None