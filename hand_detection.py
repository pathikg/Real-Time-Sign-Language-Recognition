import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height = 480
    frame_width = 640
    frame = cv2.resize(frame, (frame_width, frame_height))

    cv2.rectangle(frame, (350, 120), (620, 400), (0, 255, 0), 2)
    cv2.imshow('Original', frame)

    roi = frame[120:400, 350:620]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.GaussianBlur(roi, (5, 5), 0)

    ret, thresh = cv2.threshold(roi, 127, 255, 0)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('thresh', thresh)

    roi_edges = cv2.Canny(roi, 100, 200)
    cv2.imshow('Edges', roi_edges)

    cv2.drawContours(roi, contours, -1, (0, 255, 0), 3)
    cv2.imshow('roi', roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
