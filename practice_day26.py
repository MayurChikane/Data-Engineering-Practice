print("------------------------ Practice Day 26 ------------------------") 

# Image color editing app 

import cv2
import numpy as np
def color_editing_app():
    img = cv2.imread("D:\Documents\Mayur.png")
    if img is None:
        print("❌ Could not read the image.")
        return
    print("✅ Image loaded successfully.")
    print("Applying color transformations...")
    # Increase brightness
    bright_img = cv2.convertScaleAbs(img, alpha=1.2, beta=50)
    # Increase contrast
    contrast_img = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
    # Convert to HSV and adjust saturation
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_img[:, :, 1] = cv2.add(hsv_img[:, :, 1], 50)  # Increase saturation
    saturated_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    # Save processed images
    cv2.imwrite('bright_image.jpg', bright_img)
    cv2.imwrite('contrast_image.jpg', contrast_img)
    cv2.imwrite('saturated_image.jpg', saturated_img)
    print("✅ Processed images saved: bright_image.jpg, contrast_image.jpg, saturated_image.jpg")
    cv2.imshow('Original Image', img)
    cv2.imshow('Brightened Image', bright_img)
    cv2.imshow('Contrast Enhanced Image', contrast_img)
    cv2.imshow('Saturated Image', saturated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("👋 Color editing completed.")
    
if __name__ == "__main__":
    color_editing_app()