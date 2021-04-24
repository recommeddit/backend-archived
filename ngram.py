import numpy as numpy
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix

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
