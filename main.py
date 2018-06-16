import os

import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import Dropout
#from keras.layers import LSTM
#from keras.callbacks import ModelCheckoint
#from keras.utils import np_utils
from collections import Counter
import pickle
#pickle module for serialising and de-serialisring python projects

#Load .txt file with aprox 150 Donald Trump tweet (June 3rd - June 16th)
filename = open('trumptweets.txt') #encoding='uft-8')
data = filename.read()

#all chars will be in lowercase + new line chars removed
data = data.lower()
data = data.replace('\n', ' ')

filename.close()

#char counter
number_chars = len(data)
print("Char count in tweets", number_chars)

#find unique chars
chars_set = set(data)
unique_chars = len(chars_set)

#char frequencies
chars_frequency_dictionary = Counter(data)
char_list_by_frequency = list(chars_frequency_dictionary.keys())
#print(char_list_by_frequency)

char_index = list(range(0, len(chars_set)))
char_index = [i+1 for i in char_index]
print(char_index)

char_dictionary = {}
for key, value in zip(char_list_by_frequency, char_index):
    char_dictionary[key] = []
    char_dictionary[key].append(value)
print(char_dictionary)

index_dictionary = {}
for key, value in zip(char_index, char_list_by_frequency):
    index_dictionary[key] = []
    index_dictionary[key].append(value)

#saving dictionaries
with open('char_dictionary.pkl', "wb") as f:
    pickle.dump(char_dictionary, f)

with open('char_index_dictionary.pkl', "wb") as f:
    pickle.dump(index_dictionary, f)


current_directory = os.getcwd()
data_dir = 'char_sentences'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)
os.chdir(data_dir)



max_length = 280
min_length = 100
tokenised_string = []
loop_count = 0
for c in data:
    token = char_dictionary.get(c)
    tokenised_string.append(token)

    if c == '?' or c == '.' or c == '!' or c == ',':
        loop_count += 1
        file_name = 'char_%s' % str(loop_count)
        flattened = [y for x in tokenised_string for y in x]
        np.save(file_name, flattened)
        if len(tokenised_string) > max_length: max_length = len(tokenised_string)
        if len(tokenised_string) < min_length: min_length = len(tokenised_string)
        tokenised_string = []

print("min/max", max_length, min_length)

file_list = os.listdir(os.getcwd())
print(file_list)
count = 0
for f in file_list:
    count += 1
    if count > 10: break
    test = np.load(f)
    print(test)
    print("******")




