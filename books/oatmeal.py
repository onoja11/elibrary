import cv2
from pyzbar.pyzbar import decode
import os

def barcode_scan(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        return f"File '{image_path}' not found!"
    
    # Load the image from the provided path
    img = cv2.imread(image_path)
    
    # Check if the image was successfully loaded
    if img is None:
        return "Image not found or unable to open!"
    
    # Detect barcodes in the image
    detectedBarcodes = decode(img)
    
    if not detectedBarcodes:
        return "Barcode Not Detected or your barcode is blank/corrupted!"
    else:
        # Traverse through all the detected barcodes in the image
        for barcode in detectedBarcodes:
            # Locate the barcode position in the image
            (x, y, w, h) = barcode.rect
            
            # Draw a rectangle around the detected barcode
            cv2.rectangle(img, (x - 10, y - 10), 
                          (x + w + 10, y + h + 10), 
                          (255, 0, 0), 2)
            
            if barcode.data != "":
                # Print the barcode data and type
                print(f"Barcode Data: {barcode.data.decode('utf-8')}")
                print(f"Barcode Type: {barcode.type}")
        
        # Display the image with the highlighted barcode
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage


print(barcode_scan('download (1).png'))