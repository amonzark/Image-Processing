import cv2
from image_utils import load_image, save_image

gambar = 'images.jpg'
img = load_image(gambar)

if img is not None:
    print("Displaying original image...")
    cv2.imshow('Image', img)
    cv2.waitKey(10000)
    save_image('save/output.jpg', img)

    print("Displaying converted image to grayscale...")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(10000)
    save_image('save/grayscale.jpg', gray)

    print("Displaying converted image to RGB...")
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('RGB Image', rgb)
    cv2.waitKey(10000)
    save_image('save/rgb.jpg', rgb)

    print("Displaying converted image to HSV...")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', hsv)
    cv2.waitKey(10000)
    save_image('save/hsv.jpg', hsv)

    cv2.destroyAllWindows()
