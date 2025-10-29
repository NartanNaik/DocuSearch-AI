import cv2
import os
import pytesseract # Import the pytesseract library

# --- IMPORTANT: CONFIGURE TESSERACT PATH ---
# If we didn't add Tesseract to our system PATH, we MUST tell pytesseract where to find it.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Example path


IMAGE_PATH = "image.webp" # Or sample_doc.png, whatever we test image is

# --- Step 1: Load the Image ---
if os.path.exists(IMAGE_PATH):
    print(f"Loading image: {IMAGE_PATH}")
    image_color = cv2.imread(IMAGE_PATH)

    if image_color is not None:
        print("Color image loaded successfully!")
        # ... (dimensions print)

        # --- Step 2: Convert to Grayscale ---
        print("Converting image to grayscale...")
        image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
        print("Grayscale conversion successful!")
        # ... (dimensions print)

        # --- Step 3: Apply Thresholding ---
        print("Applying thresholding...")
        ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

        if ret:
             print("Thresholding successful!")
             # ... (dimensions print)

             print("Image pre-processing complete.")

             # --- Step 4: Perform OCR with Tesseract ---
             print("Performing OCR...")
             try:
                 # Use pytesseract to extract text from the thresholded image
                 extracted_text = pytesseract.image_to_string(image_thresh)

                 print("\n--- Extracted Text ---")
                 print(extracted_text)
                 print("--- End of Text ---\n")
                 print("OCR successful!")

                 # TODO: Next step - Store the extracted_text (e.g., in MongoDB)
                 # TODO: Next step - Build basic frontend for keyword search

             except pytesseract.TesseractNotFoundError:
                 print("\n--- TESSERACT ERROR ---")
                 print("Tesseract is not installed or not in your PATH.")
                 print("Please install Tesseract OCR engine and configure the path if needed (see code comments).")
             except Exception as e:
                 print(f"\nAn error occurred during OCR: {e}")

        else:
            print("Error during thresholding.")
    else:
        print(f"Error: Could not read the image file: {IMAGE_PATH}")
else:
    print(f"Error: Image file not found at: {IMAGE_PATH}")