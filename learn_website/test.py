#!/usr/bin/python
#coding:utf-8
import sys
sys.path.append("..")
import os
import re
import shutil
import time 
import math
import csv
import numpy as np
#import tensorflow as tf
#import keras.backend.tensorflow_backend as KTF
#import file_read

from pandas import read_csv
from matplotlib import pyplot
# load dataset
dataset = read_csv('pollution.csv', header=0, index_col=0)
values = dataset.values

print dataset
print values

print values [:, 4]
print values [:, :-1]

print np.random.random((10, 5))

"""
# specify columns to plot
groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.show()
"""
