from collections import  Counter
from collections import OrderedDict
import operator

import  numpy as np
import pickle
import csv


file = open('trumptweets.txt')#, encoding='utf-8')
data = file.read()

data = data.lower()
data = data.replace('\n', ' ')

data = data.replace('#', ' ')
data = data.replace('@', ' ')
data = data.replace('!', ' ')
data = data.replace('?', ' ')

file.close()

#Amount of words in all tweets
words = data.split()
words_number = len(words)
print("Amounts of words in tweets are: ", len(words))

#Amount of unique words found in tweets
words_set = set(words)
unique_words = len(words_set)
print("Amount of unique words: ", len(words_set))

count = Counter(words)
print(count)

with open('word_counter.csv', 'w') as f:
    [f.write('{0}, {1}\n'.format(key, value)) for key, value in count.items()]

frequency = {}
for k, v in count.items():
    frequency[k] = v/words_number*100

with open('word_frequency.csv', 'w') as f:
    [f.write('{0}, {1}\n'.format(key, value)) for key, value in frequency.items()]

sorted_list = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_list)

with open('sorted_word_frequency.csv', 'w') as f:
    for i in sorted_list:
        row = "%s, %f\n" % (i[0], i[1])
        print(row)
        f.write(row)