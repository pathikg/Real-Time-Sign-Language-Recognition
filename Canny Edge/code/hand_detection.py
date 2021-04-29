import cv2
import numpy as np
import matplotlib.pyplot as plt
from model import predict


def capture():
    sen = ''
    cap = cv2.VideoCapture(0)
    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height = 480
        frame_width = 640
        # a standard frame window of size 640*480
        frame = cv2.resize(frame, (frame_width, frame_height))

        # drawing a rectangle in a frame which will capture hand
        cv2.rectangle(frame, (300, 100), (500, 300), (0, 300, 0), 2)

        # rectangle of background of text s
        cv2.rectangle(frame, (0, 0), (300, 50), (0, 0, 0), -1)
        frame = cv2.putText(frame, 'press q to exit', (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 255), 1, cv2.LINE_AA)

        # region of interest i.e rectangle which we drawn earlier
        roi = frame[100:300, 300:500]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi = cv2.GaussianBlur(roi, (5, 5), 0)

        # contours
        # ret, thresh = cv2.threshold(roi, 127, 255, 0)
        # contours, hierarchy = cv2.findContours(
        #     thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.imshow('thresh', thresh)

        # applying edge detection on roi
        roi_edges = cv2.Canny(roi, 100, 200)
        # cv2.imshow('Edges', roi_edges)

        # cv2.drawContours(roi, contours, -1, (0, 255, 0), 3)
        # cv2.imshow('roi', roi)

        # resizing input to (100,100) since that's the image size required for model
        roi_edges = cv2.resize(roi_edges, (200, 200))
        # print(roi.shape)

        # to make roid_edges of shape (200,200,1) , speicifying color channel which is required for model
        img = np.expand_dims(roi_edges, axis=2)
        cv2.imshow('input for model', img)

        frame = cv2.putText(frame, predict(img), (300, 400), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 255), 1, cv2.LINE_AA)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            sen += predict(img)
            print(sen)

        frame = cv2.putText(frame, sen, (300, 500),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow('Smile', frame)

    cv2.destroyAllWindows()
    cap.release()


# capture()
