
# coding: utf-8

text = open('ticking_spotify.txt').read()
sents = [line.strip() for line in text.splitlines()]
lines = [line.strip() for line in open('building_global_community.txt')]


import nltk

from nltk import word_tokenize
words = []
for line in lines :
    split_words = word_tokenize(line)
    words.append(split_words)


for sentence in words:
    for word in sentence:
        sentence[sentence.index(word)] = word.lower()

from nltk.corpus import stopwords 
stopwords = set(stopwords.words('english'))

filted_words = []
for sentence in words :
    for word in sentence:
        if word.isalpha() or word.isdigit() or word.isalnum():
            if word not in stopwords:
                filted_words.append(word)

filted_words

from collections import Counter

counter = Counter(filted_words)
counter.most_common(20)

