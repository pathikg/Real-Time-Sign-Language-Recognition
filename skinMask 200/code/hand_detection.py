import cv2
import numpy as np
from model import predict


def capture():
    s = ''
    k = 0
    cap = cv2.VideoCapture(0)
    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height = 480
        frame_width = 640
        # a standard frame window of size 640*480
        frame = cv2.resize(frame, (frame_width, frame_height))

        # drawing a rectangle in a frame which will capture hand
        cv2.rectangle(frame, (400, 100), (600, 300), (0, 255, 0), 2)

        # rectangle of background of text s
        cv2.rectangle(frame, (0, 0), (300, 50), (0, 0, 0), -1)
        frame = cv2.putText(frame, 'press q to exit', (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 255), 1, cv2.LINE_AA)

        # region of interest i.e rectangle which we drawn earlier
        roi = frame[100:300, 400:600]

        # extracting hand from roi
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 58, 50], dtype=np.uint8)
        upper_skin = np.array([30, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        kernel = np.ones((4, 4), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=4)
        mask = cv2.GaussianBlur(mask, (5, 5), 100)
        mask = np.expand_dims(mask, axis=2)
        cv2.rectangle(frame, (290, 370), (330, 410), (0, 0, 0), -1)
        frame = cv2.putText(frame, predict(mask), (300, 400), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 255), 1, cv2.LINE_AA)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('d'):
            s += predict(mask)
            k = + 20
        elif key == ord('s'):
            s += ' '
        elif key == ord('a'):
            if len(s) > 0:
                s = list(s)
                i = s.pop()
                s = ''.join(s)
        elif key == ord('c'):
            s = ''

        # cv2.rectangle(frame, (290, 370), (330, 410), (0, 0, 0), -1)
        x_org = 300-k 
        frame = cv2.putText(frame, s, (x_org, 450), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 0), 1, cv2.LINE_AA)

        cv2.imshow('Smile', frame)
        cv2.imshow('roi', mask)

    cv2.destroyAllWindows()
    cap.release()


capture()
