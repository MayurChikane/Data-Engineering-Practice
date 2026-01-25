print("---------------------------- Practice Day 27 ----------------------------")

# Image blending app
import cv2
import numpy as np
def image_blending_app():
    img1 = cv2.imread("D:\Documents\Mayur.png")
    img2 = cv2.imread("C:\\Users\\mayur\\OneDrive\\Pictures\\Screenshots\\prajwal.jpg")
    if img1 is None or img2 is None:
        print("❌ Could not read one or both images.")
        return
    print("✅ Images loaded successfully.")
    print("Resizing second image to match the first image...")
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    alpha = 0.5
    beta = 1.0 - alpha
    print("Blending images with alpha =", alpha, "and beta =", beta)
    blended_img = cv2.addWeighted(img1, alpha, img2_resized, beta, 0.0)
    cv2.imwrite('blended_image.jpg', blended_img)
    print("✅ Blended image saved: blended_image.jpg")
    cv2.imshow('Image 1', img1)
    cv2.imshow('Image 2', img2_resized)
    cv2.imshow('Blended Image', blended_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("👋 Image blending completed.")
    
if __name__ == "__main__":
    image_blending_app()