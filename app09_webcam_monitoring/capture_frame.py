import cv2
import numpy as np


# Khởi tạo video capture từ camera (0 là camera mặc định)
video = cv2.VideoCapture(0)

# Chờ cho đến khi capture được frame
while True:
    # Đọc frame từ video stream
    check, frame = video.read()
    
    # Hiển thị frame
    cv2.imshow("Frame", frame)
    
    # Chờ phím nhấn
    key = cv2.waitKey(1)
    
    # Nếu phím "c" được nhấn (capture)
    if key == ord("c"):
        # Print captured frame
        print("Captured frame:")
        np.set_printoptions(threshold=np.inf)  # Print entire array
        print(frame)
        
        # Reset print options
        np.set_printoptions(threshold=1000)  # Reset threshold
        
        # Break out of loop
        break
    
    # Nếu phím "q" được nhấn (quit)
    elif key == ord("q"):
        break

# Giải phóng video capture và đóng cửa sổ hiển thị
video.release()
cv2.destroyAllWindows()
