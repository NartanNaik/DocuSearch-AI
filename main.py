import cv2
import os # To check if file exists

IMAGE_PATH = "image.webp"

# --- Step 1: Load the Image ---
if os.path.exists(IMAGE_PATH):
    print(f"Loading image: {IMAGE_PATH}")
    # Read the image from the file
    image = cv2.imread(IMAGE_PATH)

    if image is not None:
        print("Image loaded successfully!")
    
    # --- Step 2: Display the Image (Optional, just to see it worked) ---
        cv2.imshow("My Scanned Document", image)
        cv2.waitKey(0) # Wait until a key is pressed
        cv2.destroyAllWindows()

        # --- Step 3: Print its dimensions (Proof it's loaded) ---
        height, width, channels = image.shape
        print(f"Image dimensions: Width={width}, Height={height}")

        # TODO: Next step - Convert image to grayscale (cv2.cvtColor)
        # TODO: Next step - Apply thresholding (cv2.threshold)
        # TODO: Next step - Integrate Tesseract OCR
    else:
        print(f"Error: Could not read the image file: {IMAGE_PATH}")
else:
    print(f"Error: Image file not found at: {IMAGE_PATH}")