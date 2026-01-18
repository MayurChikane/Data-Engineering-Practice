print("---------------------------------- Practice Day 24 -----------------------------")

# Camera app

import cv2

def camera_app():
    # Open default camera (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    print("📷 Camera started")
    print("Press 'c' to capture image")
    print("Press 'q' to quit")

    img_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        # Show camera feed
        cv2.imshow("Python Camera App", frame)

        key = cv2.waitKey(1) & 0xFF

        # Capture image
        if key == ord('c'):
            img_name = f"capture_{img_count}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"✅ Image saved as {img_name}")
            img_count += 1

        # Quit app
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Camera closed")

if __name__ == "__main__":
    camera_app()

print("------------------------ End of Practice Day 24 ------------------------")