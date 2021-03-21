import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pickle


CATEGORIES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']


infile = open(
    r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\training_data.pkl", 'rb')
train = pickle.load(infile)
infile.close()

infile = open(
    r"E:\Pathik\KJ\sem4\MiniProject\ASL recognition\testing_data.pkl", 'rb')
test = pickle.load(infile)
infile.close()

# Creating X_train, X_test, y_train, y_test

X_train = np.zeros((len(train), 100, 100))
y_train = np.zeros((len(train), 1), dtype=int)
for i in range(len(train)):
    X_train[i] = train[i][0]
    y_train[i] = train[i][1]

X_test = np.zeros((len(test), 100, 100))
y_test = np.zeros((len(test), 1), dtype=int)
for i in range(len(test)):
    X_test[i] = test[i][0]
    y_test[i] = test[i][1]

# Resizing X_train, X_test to (len(),100,100,1) since its necessary for training and testing in model
X_train = np.expand_dims(X_train, axis=3)
X_test = np.expand_dims(X_test, axis=3)

#  model was done in google collab
model = load_model(
    'E:\Pathik\KJ\sem4\MiniProject\ASL recognition\code\model.h5')


# loss, acc = model.evaluate(X_test, y_test, verbose=2)
# print('model, accuracy: {:5.2f}%'.format(100 * acc))


def predict(img):
    # added this for image to fit input shape of (1,100,100,1)
    img = np.expand_dims(img, axis=0)
    # returns predicted character for that img
    return CATEGORIES[np.argmax(model.predict(img))]


# i = 5
# print("predictions for image in testing data at index",
#       i, ":", predict(X_test[i]))
# print("Original image in testing data at index",
#       i, ":", CATEGORIES[y_test[i][0]])
