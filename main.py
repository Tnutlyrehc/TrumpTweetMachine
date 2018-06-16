#import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import Dropout
#from keras.layers import LSTM
#from keras.callbacks import ModelCheckoint
#from keras.utils import np_utils

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


