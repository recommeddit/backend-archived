#lda technique to extract keywords
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import pandas as pd
import nltk
#nltk.download('wordnet')
stemmer = SnowballStemmer('english')

def lemmatize(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text,pos = 'v'))

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize(token)),
    
    return result

# example = 'I have to write this paper for this class'
# words = []
# for word in example.split(' '):
#     words.append(word)
# print(words)
# print(preprocess(example))

with open('sample.txt', 'r') as file:
    data = file.read()
data = preprocess(data)
data = [data]
#print(data[:2])
dictionary = gensim.corpora.Dictionary(data)
count = 0
# for k,v in dictionary.iteritems():
#     print(k,v)
#     count += 1
#     if count > 20:
#         break
