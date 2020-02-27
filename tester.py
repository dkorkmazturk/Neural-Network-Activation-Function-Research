import tensorflow as tf
from tensorflow import keras
from datetime import datetime
import h5py
import time
import sys
import os

from networks import *

#networks = [FashionMNIST, CNN_MNIST, CIFAR]

#Speed Test
networks = [FashionMNIST]

activationfunctions = [tf.nn.relu]

for network in networks:
	net = network()
	config = net.getConfig()
	((xTrain,yTrain),(xTest, yTest)) = net.getDataSet()

	for func in activationfunctions:
		model = net.buildModel(activationFucntion = func)
		model = net.compile(model)

		#local train, get checkpoints and stats


		checkpoint_path = config['path'] + "training/" + func.__name__ + "/cp-{epoch:04d}.ckpt"
		checkpoint_dir = os.path.dirname(checkpoint_path)
		cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True)

		log_dir = config['path'] +"logs/" + func.__name__ +"/"+ datetime.now().strftime("%Y%m%d-%H%M%S")
		tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)



		#model.fit(xTrain, yTrain, epochs= config['epoch'], batch_size = config['batch'],callbacks = [cp_callback])

		#Speed Train for Testin
		model.fit(xTrain, yTrain, epochs= 5, batch_size = config['batch'],validation_data =(xTest, yTest), callbacks = [cp_callback, tensorboard_callback])

		#test_loss, test_acc = model.evaluate(xTest, yTest)

		#print('Test accuracy:', test_acc)
		#model.summary()




		#measure accrucy

		#plot data
		#save data
