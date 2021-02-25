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
edges = cv2.Canny(img, 100, 200)
plt.title('edges')
plt.imshow(edges, cmap="gray")

plt.show()

# now apply this to the whole dataset
