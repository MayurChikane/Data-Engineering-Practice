print("----------------------------- Practice Day 28 ----------------------------")

# Edge detection app
import cv2
def edge_detection_app():
    img = cv2.imread("D:\Documents\Mayur.png")
    if img is None:
        print("❌ Could not read the image.")
        return
    print("✅ Image loaded successfully.")
    print("Converting image to grayscale...")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Applying Canny edge detection...")
    edges = cv2.Canny(gray_img, 100, 200)
    cv2.imwrite('edges_image.jpg', edges)
    print("✅ Edge-detected image saved: edges_image.jpg")
    cv2.imshow('Original Image', img)
    cv2.imshow('Edge Detected Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("👋 Edge detection completed.")
    
if __name__ == "__main__":
    edge_detection_app()
    
print("-------------------------- End of Practice Day 28 --------------------------")