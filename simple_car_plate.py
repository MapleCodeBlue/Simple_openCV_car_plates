import cv2
import numpy as np
import os


base_path = r''

video = cv2.VideoCapture(os.path.join(base_path, 'carplate2.mp4'))

# Load the Haar cascade for detecting plates
plate_cascade = cv2.CascadeClassifier('number_plate.xml')

while video.isOpened():
    ret, image = video.read()
    if not ret:
        break

    # Change image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect plates in the frame
    plates = plate_cascade.detectMultiScale(gray, 1.1, 3)

    # Drawing rectangles around every plates detected
    for (x, y, w, h) in plates:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, 'Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Car_plates', image)

    # Setting up to break out of the video
    end_video = cv2.waitKey(1)
    if end_video == ord('e'):
        break 

video.release()

