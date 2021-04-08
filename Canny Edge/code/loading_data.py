import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import random
import pickle


DATADIR = "E:\Pathik\KJ\sem4\MiniProject\ASL recognition\dataset"
CATEGORIES = os.listdir(DATADIR)

data = []


def load_data():
    for category in CATEGORIES:
        # create path to image of respective alphabet
        path = os.path.join(DATADIR, category)
        # get the classification  for each alphabet A : 0, B : 1, C : 2,...
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):  # iterate over each image
            img_array = cv2.imread(os.path.join(
                path, img), cv2.IMREAD_GRAYSCALE)  # convert to array
            img_array = cv2.resize(img_array, (100, 100))
            # add this to our training_data
            data.append([img_array, class_num])


load_data()


with open("E:\Pathik\KJ\sem4\MiniProject\ASL recognition\dataset.pkl", "wb") as f:
    pickle.dump(data, f)
f.close()
