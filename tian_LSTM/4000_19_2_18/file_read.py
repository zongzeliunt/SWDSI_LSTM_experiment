#!/usr/bin/python
#coding:utf-8
import os
import re

#this is generate total equal length learn and test vectors
def x_y_file_read (folder):
#{{{
	#file names
		#index_of_words.txt  index_of_y.txt  x_num_vector.txt  y_num_vector.txt
	y_cluster_num = 12
	learn_vector_ratio = 0.70
	#read files
	#{{{
	y_vector_file = folder + "/y_num_vector.txt"
	fl = open(y_vector_file, "r")
	y_vectors = fl.readlines()
	x_vector_file = folder + "/x_num_vector.txt"
	fl = open(x_vector_file, "r")
	x_vectors = fl.readlines()
	#}}}
	
	#collect total_vector	
	#{{{
	total_vector = {}
	learn_vector = [] 
	test_vector = []
	for i in range (0, y_cluster_num):
		total_vector[i] = []
		learn_vector.append(0)
		test_vector.append(0)
	
	total_count = 0
	for i in range(0, len(y_vectors)):
		line = y_vectors[i]
		line_num = int(line.replace("\n", ""))
		total_vector[line_num].append(i)
			#total_count += 1
			#if total_count == total_require_num:
			#	break
	#}}}

	for i in range (0, y_cluster_num):
		learn_vector[i] = int(learn_vector_ratio * float(len(total_vector[i])))
		test_vector[i] =  len(total_vector[i]) - learn_vector[i]



	#generate x_learn, y_learn, x_test, y_test
	x_learn = []
	y_learn = []
	x_test = []
	y_test = []
	step_count = 0
	#0:8667, 1:29264, 2:9403, 3:31237
	#4:37534, 5:17777, 6:1633, 7:14123
	#8:1391, 9:1370, 10:261, 11:16	
	

	for y_class_num in range (0, 12):
		#this range is 0 to 12 
		if y_class_num == 6:
			continue
		if y_class_num == 8:
			continue
		if y_class_num == 9:
			continue
		if y_class_num == 10:
			continue
		if y_class_num == 11:
			#class 11 have only 16 times, abandon!
			#ignore class 11
			continue
		insert_y_class_num = 0 
		if (y_class_num == 7):
			insert_y_class_num = 6
		else:
			insert_y_class_num = y_class_num
		"""
		
		if y_class_num == 1: 
			insert_y_class_num = 0
		elif y_class_num == 3: 
			insert_y_class_num = 1 
		elif y_class_num == 4:
			insert_y_class_num = 2 
		elif y_class_num == 5:
			insert_y_class_num = 3 
		elif y_class_num == 7:
			insert_y_class_num = 4 
		else:
			continue
		"""
		
		insert_test_step_num = learn_vector[y_class_num] / test_vector[y_class_num]
		step_num = 0
		total_learn_count = 0
		total_test_count = 0
		for class_internal_count in range (0, len(total_vector[y_class_num])):	
			this_y_vector_number = total_vector[y_class_num][class_internal_count]
			precessed_x_vector = []
			x_vector = x_vectors[this_y_vector_number].replace("\n", "")
			for element in x_vector.split():
				precessed_x_vector.append(int(element))




			if step_num != insert_test_step_num and total_learn_count < learn_vector[y_class_num]:
				y_learn.append(insert_y_class_num)
				x_learn.append(precessed_x_vector)
				total_learn_count += 1
				if total_test_count < test_vector[y_class_num]:
					step_num += 1
			elif step_num == insert_test_step_num and total_test_count < test_vector[y_class_num]:
				if (y_class_num != 7):
					break
				y_test.append(insert_y_class_num)
				x_test.append(precessed_x_vector)
				total_test_count += 1
				step_num = 0
				


			"""
			#we use this_y_vector_number to search x_vector 
			if not class_internal_count > learn_vector[y_class_num]:
				y_learn.append(insert_y_class_num)
				x_learn.append(precessed_x_vector)
			else:

				if (y_class_num != 7):
					break
				y_test.append(insert_y_class_num)
				x_test.append(precessed_x_vector)
			"""
 
	return x_learn, y_learn, x_test, y_test
#}}}	


def x_y_file_read_bak_1 (folder):
#{{{
	#file names
		#index_of_words.txt  index_of_y.txt  x_num_vector.txt  y_num_vector.txt
	y_cluster_num = 12
	learn_vector_ratio = 0.7
	#read files
	#{{{
	y_vector_file = folder + "/y_num_vector.txt"
	fl = open(y_vector_file, "r")
	y_vectors = fl.readlines()
	x_vector_file = folder + "/x_num_vector.txt"
	fl = open(x_vector_file, "r")
	x_vectors = fl.readlines()
	#}}}
	
	#collect total_vector	
	#{{{
	total_vector = {}
	learn_vector = [] 
	test_vector = []
	for i in range (0, y_cluster_num):
		total_vector[i] = []
		learn_vector.append(0)
		test_vector.append(0)
	
	total_count = 0
	for i in range(0, len(y_vectors)):
		line = y_vectors[i]
		line_num = int(line.replace("\n", ""))
		total_vector[line_num].append(i)
			#total_count += 1
			#if total_count == total_require_num:
			#	break
	#}}}

	for i in range (0, y_cluster_num):
		learn_vector[i] = int(learn_vector_ratio * float(len(total_vector[i])))
		test_vector[i] =  len(total_vector[i]) - learn_vector[i]



	#generate x_learn, y_learn, x_test, y_test
	x_learn = []
	y_learn = []
	x_test = []
	y_test = []
	step_count = 0
	#0:8667, 1:29264, 2:9403, 3:31237
	#4:37534, 5:17777, 6:1633, 7:14123
	#8:1391, 9:1370, 10:261, 11:16	
	

	for y_class_num in range (0, 12):
		#this range is 0 to 12 
		if y_class_num == 6:
			continue
		if y_class_num == 8:
			continue
		if y_class_num == 9:
			continue
		if y_class_num == 10:
			continue
		if y_class_num == 11:
			#class 11 have only 16 times, abandon!
			#ignore class 11
			continue
		for class_internal_count in range (0, len(total_vector[y_class_num])):	
			this_y_vector_number = total_vector[y_class_num][class_internal_count]
			precessed_x_vector = []
			x_vector = x_vectors[this_y_vector_number].replace("\n", "")
			for element in x_vector.split():
				precessed_x_vector.append(int(element))

			
			insert_y_class_num = 0 
			if (y_class_num == 7):
				insert_y_class_num = 6
			else:
				insert_y_class_num = y_class_num



			#we use this_y_vector_number to search x_vector 
			if not class_internal_count > learn_vector[y_class_num]:
				y_learn.append(insert_y_class_num)
				x_learn.append(precessed_x_vector)
			else:
				if (y_class_num != 4):
					break
				y_test.append(insert_y_class_num)
				x_test.append(precessed_x_vector)
 
	return x_learn, y_learn, x_test, y_test
#}}}	

def x_y_file_read_bak (folder):
#{{{
	#file names
		#index_of_words.txt  index_of_y.txt  x_num_vector.txt  y_num_vector.txt
	#needed numbers
	#total 12 classes
	y_cluster_num = 12	
	learning_total_num = 6000
	testing_total_num = 2000
	learn_vs_test_step = learning_total_num/testing_total_num
	vector_total_num = learning_total_num + testing_total_num
	total_require_num = vector_total_num * y_cluster_num

	#read files
	#{{{
	y_vector_file = folder + "/y_num_vector.txt"
	fl = open(y_vector_file, "r")
	y_vectors = fl.readlines()
	x_vector_file = folder + "/x_num_vector.txt"
	fl = open(x_vector_file, "r")
	x_vectors = fl.readlines()
	#}}}
	
	#collect total_vector from y	
	#{{{
	total_vector = {}
	for i in range (0, y_cluster_num):
		total_vector[i] = []
	total_count = 0
	for i in range(0, len(y_vectors)):
		line = y_vectors[i]
		line_num = int(line.replace("\n", ""))
		#if not len(total_vector[line_num]) ==  vector_total_num:
		total_vector[line_num].append(i)
			#total_count += 1
			#if total_count == total_require_num:
			#	break
	#}}}
	#generate x_learn, y_learn, x_test, y_test
	x_learn = []
	y_learn = []
	x_test = []
	y_test = []
	step_count = 0
	#0:8667, 1:29264, 2:9403, 3:31237
	#4:37534, 5:17777, 6:1633, 7:14123
	#8:1391, 9:1370, 10:261, 11:16	

	for class_internal_count in range (0, vector_total_num):
		#if one class require 10 learn and 3 test, this range is 0 to 13	
		for y_class_num in range (0, 12):
			#this range is 0 to 12 
			if y_class_num == 6:
				continue
			if y_class_num == 8:
				continue
			if y_class_num == 9:
				continue
			if y_class_num == 10:
				continue
			if y_class_num == 11:
				#class 11 have only 16 times, abandon!
				#ignore class 11
				continue
			
			this_y_vector_number = total_vector[y_class_num][class_internal_count]
			precessed_x_vector = []
			x_vector = x_vectors[this_y_vector_number].replace("\n", "")
			for element in x_vector.split():
				precessed_x_vector.append(int(element))

			if y_class_num == 7:
				#replace class 6 to 7
				y_class_num = 6
			
			#we use this_y_vector_number to search x_vector 
			if not step_count == learn_vs_test_step:
				y_learn.append(y_class_num)
				x_learn.append(precessed_x_vector)
			else:
				y_test.append(y_class_num)
				x_test.append(precessed_x_vector)
		
		if not step_count == learn_vs_test_step:
			step_count += 1
		else:
			step_count =0

 
	return x_learn, y_learn, x_test, y_test
#}}}	
