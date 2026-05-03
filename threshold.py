import cv2
from image_utils import display_image, save_image
from convert_color import convert_image_color_to_grayscale
from blurring import bilateral_blur

def apply_threshold(image):
    try:
        if image is not None:
            # Convert to grayscale
            gray = convert_image_color_to_grayscale(image)
            # Apply binary threshold
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            print(f"Threshold shape: {thresh.shape}")
            display_image(thresh)
            save_image('save/threshold.jpg', thresh)
        else:
            print("Failed to load image for thresholding.")
    except Exception as e:
        print(f"Error occurred during thresholding: {e}")

def apply_threshold_inverse(image):
    try:
        if image is not None:
            # Convert to grayscale
            gray = convert_image_color_to_grayscale(image)
            # Apply binary threshold
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            print(f"Threshold shape: {thresh.shape}")
            display_image(thresh)
            save_image('save/threshold_inverse.jpg', thresh)
        else:
            print("Failed to load image for thresholding.")
    except Exception as e:
        print(f"Error occurred during thresholding: {e}")

def apply_threshold_otsu(image):
    try:
        if image is not None:
            # Convert to grayscale
            gray = convert_image_color_to_grayscale(image)
            # Apply Otsu's thresholding
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            print(f"Threshold shape: {thresh.shape}")
            display_image(thresh)
            save_image('save/threshold_otsu.jpg', thresh)
        else:
            print("Failed to load image for thresholding.")
    except Exception as e:
        print(f"Error occurred during thresholding: {e}")

def apply_threshold_adaptive(image):
    try:
        if image is not None:
            # Convert to grayscale
            gray = convert_image_color_to_grayscale(image)
            # Apply adaptive thresholding
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            print(f"Threshold shape: {thresh.shape}")
            display_image(thresh)
            save_image('save/threshold_adaptive.jpg', thresh)
        else:
            print("Failed to load image for thresholding.")
    except Exception as e:
        print(f"Error occurred during thresholding: {e}")

def proper_thresholding(image):
    try:
        if image is not None:
            # Convert to grayscale
            gray = convert_image_color_to_grayscale(image)
            # clean the noise
            clean = bilateral_blur(gray, 9, 75, 75)
            # Apply adaptive thresholding
            thresh = cv2.adaptiveThreshold(clean, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            print(f"Threshold shape: {thresh.shape}")
            display_image(thresh)
            save_image('save/threshold_proper.jpg', thresh)
        else:
            print("Failed to load image for thresholding.")
    except Exception as e:
        print(f"Error occurred during thresholding: {e}")
