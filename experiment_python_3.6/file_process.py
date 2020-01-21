import numpy as np
import nltk, itertools, csv

TXTCODING = 'utf-8'
unknown_token = 'UNKNOWN_TOKEN'
start_token = 'START_TOKEN'
end_token = 'END_TOKEN'

dict_size = 4000
class tokenFile2vector:
	def __init__(self, file_path, dict_size):
		self.file_path = file_path
		self.dict_size = dict_size

	def _get_sentences(self):
		vector_x = []
		vector_y = []
		with open(self.file_path, 'r') as f:
			reader = csv.reader(f, skipinitialspace=True)
			next(reader)
			#sents = itertools.chain(*[nltk.sent_tokenize(x[0].decode(TXTCODING).lower()) for x in reader])
			for record in reader:
				vector_x.append(record[5])
				vector_y.append(record[1])
			print ("get {} sentences." .format(len(vector_x))) 	
			return vector_x, vector_y
	
	def	_get_x_words_dict(self, vector_x):
		#sent_words = [nltk.word_tokenize(x.decode(TXTCODING).lower()) for x in vector_x]
		sent_words = [nltk.word_tokenize(x.lower()) for x in vector_x]
		word_freq = nltk.FreqDist(itertools.chain(*sent_words))
		print ('Get {} words.'.format(len(word_freq)))
		
		common_words = word_freq.most_common(self.dict_size-1)
		dict_words = [word[0] for word in common_words]
		dict_words.append(unknown_token)
		index_of_words = dict((word, ix) for ix, word in enumerate(dict_words))
		return sent_words, dict_words, index_of_words

	def convert_x_vector (self, vector_x):
		sent_words, dict_words, index_of_words = self._get_x_words_dict(vector_x)
		for i, words in enumerate(sent_words):
			sent_words[i] = [w if w in dict_words else unknown_token for w in words]
		X_num_vector = np.array([[index_of_words[w] for w in sent[:-1]] for sent in sent_words])
		fl = open("index_of_words.txt", "w")
		for word in index_of_words:
			tmp = str(word) + " " + str(index_of_words[word]) + "\n"
			fl.write(tmp)
		fl.close()

		fl = open("x_num_vector.txt", "w")
		for vector in X_num_vector:
			tmp = ""
			for num in vector:
				tmp += str(num) + " "
			tmp += "\n"
			fl.write(tmp)
		fl.close()
		
		return index_of_words, X_num_vector

	def convert_y_vector (self, vector_y):
		Y_num_vector = []
		index_of_y = {}
		for y in vector_y:
			if y in index_of_y:
				y_num = index_of_y[y]
			else:
				y_num = len(index_of_y)
				index_of_y[y] = y_num
			Y_num_vector.append(y_num)
		fl = open("index_of_y.txt", "w")
		for y in index_of_y:
			tmp = str(y) + ": " + str(index_of_y[y]) + "\n"
			fl.write(tmp)
		fl.close()
		
		fl = open("y_num_vector.txt", "w")
		for vector in Y_num_vector:
			fl.write(str(vector) + "\n")
		fl.close()
		return index_of_y, Y_num_vector

def csv_process ():
	#file_path = r'test.csv'
	file_path = r'Consumer_Complaints_with_Consumer_Complaint_Narratives2.csv'
	myTokenFile = tokenFile2vector(file_path, dict_size)
	vector_x, vector_y = myTokenFile._get_sentences()

	index_of_words, X_num_vector = myTokenFile.convert_x_vector(vector_x)
	index_of_y, Y_num_vector = myTokenFile.convert_y_vector(vector_y)

def sentence_summary ():
	file_path = r'Consumer_Complaints_with_Consumer_Complaint_Narratives2.csv'
	myTokenFile = tokenFile2vector(file_path, dict_size)
	vector_x, vector_y = myTokenFile._get_sentences()
	longest = 0
	shortest = 9999
	total_word = 0
	total_lines = 0
	average = 0
	for line in vector_x:
		length = len(line)
		total_word += length
		if length > longest:
			longest = length
		if length < shortest:
			shortest = length
		total_lines += 1
	print (total_word)
	print (total_lines)
	print (total_word / total_lines)
	print ("longest " + str(longest))
	print ("shortest " + str(shortest))
	

	

csv_process()
#sentence_summary()

