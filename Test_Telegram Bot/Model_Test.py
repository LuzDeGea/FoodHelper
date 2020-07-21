# Imports
from pprint import pprint

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

model = load_model("fruits_model.h5")

img = keras.preprocessing.image.load_img(
    "FileSysag\\Banane.jpg", target_size=(25,25)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
pre_classes = predictions.argmax(axis=-1)
pprint(pre_classes)
