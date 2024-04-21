import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None

def saveFrameToTxtFileAndImage(frame):
    flattened_array = frame.reshape(-1, frame.shape[-1])
    np.savetxt('output.txt', flattened_array, fmt='%d')
    cv2.imwrite('output.png', frame)

def createImageFromArray(array):
    arr = np.array(array)
    cv2.imwrite('created_iamge.png',arr)
    np.save("test.txt", array)


while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # (21, 21) mức độ blur được apply
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
    
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 3000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 1)
    
    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("c"):
        # Print captured frame
        print("Frame is captured:")
        saveFrameToTxtFileAndImage(delta_frame)
        break
    if key == ord("q"):
        break
print(first_frame)
video.release()
