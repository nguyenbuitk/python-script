import cv2
import time
import numpy as np
from emailing import send_email

video = cv2.VideoCapture(0)

time.sleep(1)
status_list = []
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
    status = 0
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # This applies Gaussian blur to the grayscale frame (gray_frame) to reduce noise and smooth the image. 
    # (21, 21) mức độ blur được apply
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (19, 19), 0)
    if first_frame is None:
        first_frame = gray_frame_gau
    
    # Calculates the absolute difference between the initial background frame (first_frame) and the current frame (gray_frame_gau).
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    # Pixels with differences về cường độ above a certain threshold (60 in this case) are set to white (255), and those below the threshold are set to black (0).
    # cv2.threshold(delta_frame, 5, 255, cv2.THRESH_BINARY)[0] return threshhold value
    thresh_frame = cv2.threshold(delta_frame, 5, 255, cv2.THRESH_BINARY)[1]

    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow("origin video", frame)
    # cv2.imshow("gray_frame video", gray_frame)
    # cv2.imshow("gray_frame_gau video", gray_frame_gau)
    # cv2.imshow("delta_frame video", delta_frame)
    # cv2.imshow("thresh_frame video", thresh_frame)
    cv2.imshow("dil_frame video", dil_frame)

    # draw rectangle around detected object into frame
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 3000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 1)
        if rectangle.any():
            status = 1
        
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()
    print(status_list)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("c"):
        # Print captured frame
        print("Frame is captured:")
        saveFrameToTxtFileAndImage(delta_frame)
        break
    if key == ord("q"):
        break

video.release()
