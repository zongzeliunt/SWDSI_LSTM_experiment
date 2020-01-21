#!/usr/bin/python
#coding:utf-8
import sys
sys.path.append("..")
import os
import re
import shutil
import time 
import math
import numpy
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
import file_read

from keras.datasets import imdb
from keras.models import Sequential
from keras.models import load_model 
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

"""
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5 # 占用GPU50%的显存 
session = tf.Session(config=config)
#GPU usage: watch -n 0.1 nvidia-smi
"""

top_words = 4000
max_review_length = 300

seed = 7
numpy.random.seed(seed)


#LSTM model operations
#block_LSTM_model_train
#block_LSTM_model_test
#{{{
def block_LSTM_model_train(x_train, y_train):
#{{{
	# create the model
	embedding_vector_length = 32 
	model = Sequential()
	model.add(Embedding(top_words, embedding_vector_length, input_length=max_review_length))
	#model.add(LSTM(100))
	model.add(LSTM(150, dropout=0.2, recurrent_dropout=0.2))
	model.add(Dense(7, activation='softmax'))
	#model.add(Dense(4, activation='softmax'))
	#ARES important!
		#y的可能结果是0到6,那么这个dense就要是7
		#跟网上说的定义不一样，但是如果小于7就报错
		#暂时这么写
	model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	print(model.summary())
	model.fit(x_train, y_train, nb_epoch=5, batch_size=32)
	
	json_string = model.to_json()

	care_block_work_path = "."
	json_file_name = care_block_work_path + "/LSTM_model_json.txt"
	json_fl = open(json_file_name, "w")
	for string in json_string:
		json_fl.write(string)
	json_fl.close

	model_h5_file = care_block_work_path + "/LSTM_model.h5"
	model.save(model_h5_file)
#}}}

def block_LSTM_model_test (x_test, y_test):
#{{{
	care_block_work_path = "."
	model_h5_file = care_block_work_path + "/LSTM_model.h5"
	model = load_model(model_h5_file)


	
	# Final evaluation of the model
	total_scores = model.evaluate(x_test, y_test, verbose=0)
	#scores[1] useful, don't know what scores[0] is.
	return total_scores
#}}}

input_file = "../convert_result_" + str(top_words)
x_train, y_train, x_test, y_test = file_read.x_y_file_read( input_file )

print ("x_train_length: " + str(len(x_train)))
print ("x_test_length: " + str(len(x_test)))

x_test = sequence.pad_sequences(x_test, maxlen=max_review_length)
x_train = sequence.pad_sequences(x_train, maxlen=max_review_length)
block_LSTM_model_train(x_train, y_train)
 
total_scores = block_LSTM_model_test(x_test, y_test)

print("total Accuracy: %.2f%%" % (total_scores[1]*100))
