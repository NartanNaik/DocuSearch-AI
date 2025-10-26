import cv2
import os # To check if file exists

IMAGE_PATH = "image.webp"

# --- Step 1: Load the Image ---
if os.path.exists(IMAGE_PATH):
    print(f"Loading image: {IMAGE_PATH}")
    image_color = cv2.imread(IMAGE_PATH)

    if image_color is not None:
        print("Color image loaded successfully!")
        height, width, channels = image_color.shape
        print(f"Color Image dimensions: Width={width}, Height={height}")

        # --- Step 2: Convert to Grayscale ---
        print("Converting image to grayscale...")
        image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
        print("Grayscale conversion successful!")
        gray_height, gray_width = image_gray.shape
        print(f"Grayscale Image dimensions: Width={gray_width}, Height={gray_height}")

        # --- Step 3: Apply Thresholding (Convert to Black & White) ---
        print("Applying thresholding...")

        ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
        # 'ret' is the threshold value used (we don't need it here)
        # 'image_thresh' is the resulting black and white image

        if ret: # Check if thresholding was successful (ret is usually the threshold value)
             print("Thresholding successful!")
             thresh_height, thresh_width = image_thresh.shape
             print(f"Thresholded Image dimensions: Width={thresh_width}, Height={thresh_height}")

             # We can optionally display the thresholded image now:
             # cv2.imshow("Thresholded Document", image_thresh)
             # cv2.waitKey(0)
             # cv2.destroyAllWindows()

             # TODO: Next step - Integrate Tesseract OCR using the thresholded image
        else:
            print("Error during thresholding.")

    else:
        print(f"Error: Could not read the image file: {IMAGE_PATH}")
else:
    print(f"Error: Image file not found at: {IMAGE_PATH}")