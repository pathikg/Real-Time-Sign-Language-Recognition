import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import random
import pickle

DATADIR = "E:\Pathik\KJ\sem4\MiniProject\ASL recognition\dataset"
CATEGORIES = os.listdir(DATADIR)

with open(
        r'E:\Pathik\KJ\sem4\MiniProject\ASL recognition\skinMask 200\dataset.pkl', 'rb') as f:
    data = pickle.load(f)

plt.subplot(1, 2, 1)
plt.title('before shuffle : '+str(CATEGORIES[data[50][1]]))
plt.imshow(data[50][0], cmap="gray")

random.shuffle(data)

plt.subplot(1, 2, 2)
plt.title('after shuffle : '+str(CATEGORIES[data[50][1]]))
plt.imshow(data[50][0], cmap="gray")
plt.show()


# splitting into training and testing data

# let's split it as a 80% - 20%, train-test
t = int(len(data)*80/100)
training_data = data[:t]
testing_data = data[t:]

# storing training and testing data into a pickle file
# so that while training and testing of the model that pickle file can be loaded directly

with open(r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\skinMask 200\training_data.pkl", "wb") as f:
    pickle.dump(training_data, f)


with open(r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\skinMask 200\testing_data.pkl", "wb") as f:
    pickle.dump(testing_data, f)
