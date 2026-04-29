import cv2
from image_utils import display_image, save_image
from convert_color import convert_image_color_to_grayscale, convert_image_color_to_rgb, convert_image_color_to_hsv
from image_edit import crop_image, resize_image

gambar = 'images.jpg'
img = cv2.imread(gambar)

if img is not None:
    print("Displaying original image...")
    display_image(img)
    cv2.waitKey(10000)
    save_image('save/output.jpg', img)

    print("Displaying converted image to grayscale...")
    convert_image_color_to_grayscale(img)
    cv2.waitKey(10000)

    print("Displaying converted image to RGB...")
    convert_image_color_to_rgb(img)
    cv2.waitKey(10000)

    print("Displaying converted image to HSV...")
    convert_image_color_to_hsv(img)
    cv2.waitKey(10000)

    #croping image
    x_start = int(input("Enter x start: "))
    x_end = int(input("Enter x end: "))
    y_start = int(input("Enter y start: "))
    y_end = int(input("Enter y end: "))
    print("Displaying cropped image with "+f"coordinates: ({x_start}, {y_start}) to ({x_end}, {y_end})...")
    cropped = crop_image(img, x_start, x_end, y_start, y_end)
    display_image(cropped)
    cv2.waitKey(10000)
    save_image('save/cropped.jpg', cropped)

    #resizing image
    new_width = int(input("Enter new width: "))
    new_height = int(input("Enter new height: "))
    print("Displaying resized image...")
    resized = resize_image(img, new_width, new_height)
    display_image(resized)
    cv2.waitKey(10000)
    save_image('save/resized.jpg', resized)


    cv2.destroyAllWindows()
