print("---------------------------- Practice day 25 ----------------------------")

# Image processing with openCV
import cv2
import numpy as np
def image_processing_app():
    img = cv2.imread("D:\Documents\Mayur.png")
    if img is None:
        print("❌ Could not read the image.")
        return
    print("✅ Image loaded successfully.")
    print("Applying filters...")
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur
    blurred_img = cv2.GaussianBlur(gray_img, (7, 7),sigmaX=1.5, sigmaY=1.5)
    # Edge detection using Canny
    edges = cv2.Canny(blurred_img, 50, 150)
    # Save processed images
    cv2.imwrite('gray_image.jpg', gray_img)
    cv2.imwrite('blurred_image.jpg', blurred_img)
    cv2.imwrite('edges_image.jpg', edges)
    print("✅ Processed images saved: gray_image.jpg, blurred_image.jpg, edges_image.jpg")
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', gray_img)
    cv2.imshow('Blurred Image', blurred_img)
    cv2.imshow('Edges Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("👋 Image processing completed.")
    cap.release()
    cv2.destroyAllWindows()
    print("👋 Camera closed")
    
if __name__ == "__main__":
    image_processing_app()
    
print("------------------------ End of Practice Day 25 ------------------------")