import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import random
import pickle

DATADIR = "E:\Pathik\KJ\sem4\MiniProject\ASL recognition\dataset"
CATEGORIES = os.listdir(DATADIR)

infile = open(
    'E:\Pathik\KJ\sem4\MiniProject\ASL recognition\dataset.pkl', 'rb')
data = pickle.load(infile)
infile.close()

plt.subplot(2, 2, 1)
plt.title('before shuffle : '+str(CATEGORIES[data[50][1]]))
plt.imshow(data[50][0], cmap="gray")

random.shuffle(data)

plt.subplot(2, 2, 2)
plt.title('after shuffle : '+str(CATEGORIES[data[50][1]]))
plt.imshow(data[50][0], cmap="gray")

plt.subplot(2, 2, 3)
img = data[50][0]
Gblur = cv2.GaussianBlur(img, (5, 5), 0)
plt.title('gaussian blur')
plt.imshow(Gblur, cmap="gray")

# plt.subplot(2, 2, 4)
# mask = cv2.inRange(img, 0, 110)
# plt.title('mask')
# plt.imshow(mask, cmap="gray")

plt.subplot(2, 2, 4)
edges = cv2.Canny(Gblur, 100, 200)
plt.title('edges')
plt.imshow(edges, cmap="gray")

plt.show()

# now apply this to the whole dataset
for i in tqdm(range(len(data))):
    img = data[i][0]
    Gblur = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(Gblur, 100, 200)
    data[i][0] = edges

plt.imshow(data[10][0], cmap='gray')
plt.show()


# splitting into training and testing data

# let's split it as a 80% - 20%, train-test
t = int(len(data)*80/100)
training_data = data[:t]
testing_data = data[t:]

# storing training and testing data into a pickle file
# so that while training and testing of the model that pickle file can be loaded directly

with open(r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\Canny Edge\training_data.pkl", "wb") as f:
    pickle.dump(training_data, f)


with open(r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\Canny Edge\testing_data.pkl", "wb") as f:
    pickle.dump(testing_data, f)

