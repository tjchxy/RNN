#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import random

import numpy as np


def read_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    data = list(data)
    return data


def index_data(sentences, dictionary):
    shape = sentences.shape
    sentences = sentences.reshape([-1])
    index = np.zeros_like(sentences, dtype=np.int32)
    for i in range(len(sentences)):
        try:
            index[i] = dictionary[sentences[i]]
        except KeyError:
            index[i] = dictionary['UNK']

    return index.reshape(shape)

#vocalbulary 是read_data返回的data
def get_train_data(vocabulary, batch_size, num_steps):
    ##################
    # Your Code here
    ##################
    data,count,dictionary,reversed_dictionary=build_dataset(vocalbulary,5000)
    drop=len(data)%batch_size
    xraw = data[:-drop].reshape(batch_size,)
    yraw = data[1:-drop+1].reshape(batch_size,)
    
    epoch=len(data)//batch_size//num_steps
    for i in range(epoch):
        batch = xraw[:,i*num_steps:i*num_steps(i+1)]
        labels = yraw[:,i*num_steps:i*num_steps(i+1)]
    return batch,labels
    
#words是data，n_words是len（data）
def build_dataset(words, n_words):
    """Process raw inputs into a dataset."""
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(n_words - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        index = dictionary.get(word, 0)
        if index == 0:  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reversed_dictionary
