import numpy as np

from datetime import datetime

import pickle
import operator
import timeit
from datetime import datetime
import sys
import random

import theano as theano
import theano.tensor as T
from theano.gradient import grad_clip

import TensorFlow as tf


unique_words = 4586 +1
rng = np.random.RandomState(42)

n_hidden = 235
n_epoch = 4

learning_rate = 1e-4
adjusted_learning_rate = 0.99
frequency_adjust_learning_rate = 2000

decay = 0.95
length_text = 4
n_threshold = -1

number_of_words_to_generate = 10
dump_output = 1000
save_model = 10000




train_x = tokenized_text[0:-1]
train_y = tokenized_text[1:]

n_train = len(train_x)
print("Training examples: ", n_train)

#broken into training vectors
index = 0
x = []
y = []
for i in range(n_train):
    x.append(train_x[i : i+length_text])
    x.append(train_y[i : i+length_text])

x_t = np.array(x)
y_t = np.array(y)

def randomize_data():
    training_range = np.arrange(len(y))
    training_range = np.random.permutation(training_range)

    x_train = []
    y_train = []
    for i in training_range:
        x_train.append(x_t[i])
        y_train.append(y_t[i])
    return x_train, y_train


index_dictionary = pickle.load(open('index_dictionary.pkl', "rb"))
word_dictionary = pickle.load(open('word_dictionary.pkl', "rb"))

def words_to_index(i):
    z = index_dictionary.get(w)
    if z is None: return -1
    else: return z[0]

def index_to_word(w):
    z = index_dictionary.get(w)
    if z is None: return -1
    else: return  z[0]

v_index_to_word = np.vectorize(index_to_word)
v_word_to_index = np.vectorize(words_to_index)

random_loss= np.log(unique_words) * length_text
print("Loss for random prediction: %f" % (random_loss))




class GRU:

    def __init__(self, n_words=unique_words, n_hidden=n_hidden, bptt_truncate=n_bptt_truncate):

    self.n_words = n_words
    self.n_hidden = n_hidden
    self.bptt_truncate = bptt_truncate
    n_gates = 3
    n_layers = 1





















