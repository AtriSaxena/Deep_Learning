# For loading the keras model which we have saved & json file.
import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow
import tensorflow as tf


def init(): 
	json_file = open('mnist_model.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	#load weights into new model
	loaded_model.load_weights("mnist_model.h5")
	print("Loaded Model from disk")
	#compile and evaluate loaded model
	loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	graph = tf.get_default_graph()
	return loaded_model,graph