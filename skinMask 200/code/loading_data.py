import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import random
import pickle


DATADIR = r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\dataset"
CATEGORIES = os.listdir(DATADIR)

data = []


def load_data():
    for category in CATEGORIES:
        # create path to image of respective alphabet
        path = os.path.join(DATADIR, category)
        # get the classification  for each alphabet A : 0, B : 1, C : 2,...
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):  # iterate over each image
            # read image in BGR format
            img_array = cv2.imread(os.path.join(path, img))
            img_array = cv2.resize(img_array, (200, 200))

            # converting img to hsv
            hsv = cv2.cvtColor(img_array, cv2.COLOR_BGR2HSV)

            # range for skin color
            lower_skin = np.array([0, 58, 50], dtype=np.uint8)
            upper_skin = np.array([30, 255, 255], dtype=np.uint8)

            # creating a mask
            mask = cv2.inRange(hsv, lower_skin, upper_skin)

            kernel = np.ones((3, 3), np.uint8)

            # extrapolate the hand to fill dark spots within
            # traverses all sub matrix of size kernel and check if there is one element > 1 then makes everyone in that sub matrix > 1
            mask = cv2.dilate(mask, kernel, iterations=4)

            # Gaussian Blur on image
            mask = cv2.GaussianBlur(mask, (5, 5), 100)

            # add this to our training_data
            data.append([mask, class_num])
        print("{} done".format(category))


load_data()


with open(r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\skinMask 200\dataset.pkl", "wb") as f:
    pickle.dump(data, f)