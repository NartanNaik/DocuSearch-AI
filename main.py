import cv2
import os # To check if file exists

IMAGE_PATH = "image.webp" # Or image.webp, whatever your test image is

# --- Step 1: Load the Image ---
if os.path.exists(IMAGE_PATH):
    print(f"Loading image: {IMAGE_PATH}")
    # Read the image from the file
    # Read in grayscale mode directly for simplicity OR convert later

    # Option A: Read directly as grayscale
    # image = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

    # Option B: Read in color first, then convert (better for visualization)
    image_color = cv2.imread(IMAGE_PATH)

    if image_color is not None:
        print("Color image loaded successfully!")
        height, width, channels = image_color.shape
        print(f"Color Image dimensions: Width={width}, Height={height}")

        # --- Step 2: Convert to Grayscale ---
        print("Converting image to grayscale...")
        image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
        print("Grayscale conversion successful!")

        # We can optionally display the grayscale image now if we uncomment these:
        cv2.imshow("Grayscale Document", image_gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        gray_height, gray_width = image_gray.shape
        print(f"Grayscale Image dimensions: Width={gray_width}, Height={gray_height}")


        # TODO: Next step - Apply thresholding (cv2.threshold) to make it black & white
        # TODO: Next step - Integrate Tesseract OCR using the pre-processed image
    else:
        print(f"Error: Could not read the image file: {IMAGE_PATH}")
else:
    print(f"Error: Image file not found at: {IMAGE_PATH}")