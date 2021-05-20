import numpy as numpy
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from nltk.corpus import stopwords 

#removing stopwords(if but we he she)
english_stop_words = stopwords.words('english')
def remove_stop_words(corpus):
    removed_stop_words = []
    for review in corpus:
        removed_stop_words.append(
            ' '.join([word for word in review.split()
                        if word not in english_stop_words]))
    return removed_stop_words

#print(remove_stop_words('bromwell high is a cartoon comedy'))

def stemming():
    return 0
                        
def split(inputstring):
    wordlist = inputstring.split()
    return wordlist
def getNGrams(wordlist, n): #wordlist is split words, n is the n in n-gram
    ngrams = []
    for i in range(len(wordlist) - (n-1)):
        ngrams.append(wordlist[i:i+n])
    return ngrams

teststring = 'hello it is a very nice day'
#print(getNGrams(teststring.split(),3))

vect = CountVectorizer()
