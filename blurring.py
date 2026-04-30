import cv2
from image_utils import display_image, save_image

def gaussian_blur(image, kernel_size):
    if image is not None:
        print(f"Applying Gaussian Blur with kernel size: {kernel_size}x{kernel_size}")
        blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        print(f"Blurred shape: {blurred.shape}")
        display_image(blurred)
        save_image('save/gaussian_blurred.jpg', blurred)
        return blurred
    else:
        print("Failed to load image for blurring.")
        return None
    
def median_blur(image, kernel_size):
    if image is not None:
        print(f"Applying Median Blur with kernel size: {kernel_size}x{kernel_size}")
        blurred = cv2.medianBlur(image, kernel_size)
        print(f"Blurred shape: {blurred.shape}")
        display_image(blurred)
        save_image('save/median_blurred.jpg', blurred)
        return blurred
    else:
        print("Failed to load image for median blurring.")
        return None
    
def bilateral_blur(image, diameter, sigma_color, sigma_space):
    if image is not None:
        print(f"Applying Bilateral Blur with diameter: {diameter}, sigma_color: {sigma_color}, sigma_space: {sigma_space}")
        blurred = cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)
        print(f"Blurred shape: {blurred.shape}")
        display_image(blurred)
        save_image('save/bilateral_blurred.jpg', blurred)
        return blurred
    else:
        print("Failed to load image for bilateral blurring.")
        return None

def average_blur(image, kernel_size):
    if image is not None:
        print(f"Applying Average Blur with kernel size: {kernel_size}x{kernel_size}")
        blurred = cv2.blur(image, (kernel_size, kernel_size))
        print(f"Blurred shape: {blurred.shape}")
        display_image(blurred)
        save_image('save/average_blurred.jpg', blurred)
        return blurred
    else:
        print("Failed to load image for average blurring.")
        return None