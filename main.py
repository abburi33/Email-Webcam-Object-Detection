import cv2
import time

# To start video
# For main camera 0, Webcam 1
video = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow("My Video", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
