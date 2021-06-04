import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # comment out if you don't want to see all error messages from tensorflow
from tensorflow.keras.models import load_model
import numpy as np

CATEGORIES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']


def predict(img):
    # added this for image to fit input shape of (1,200,200,1)
    img = np.expand_dims(img, axis=0)
    # returns predicted character for that img
    return CATEGORIES[np.argmax(model.predict(img))]


#  model was done in google collab
model = load_model(
    r'E:\Pathik\KJ\sem4\MiniProject\ASL recognition\skinMask 200\model_30epoch.h5')

# saver = tf.train.Saver()
# sess = tf.keras.backend.get_session()
# saver.restore(sess,r'E:\Pathik\KJ\sem4\MiniProject\ASL recognition with skinMask200\keras session\session.ckpt')
