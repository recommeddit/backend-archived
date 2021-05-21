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
# data = ['how','how','is','really','world']
dictionary = gensim.corpora.Dictionary(data)

# count = 0
# for k,v in dictionary.iteritems():
#     print(k,v)
#     count += 1
#     if count > 20:
#         break

#work on COUNT of most common words 
print(dictionary[0])
bow_corpus = [dictionary.doc2bow(doc) for doc in dictionary]
document_num = 20
bow_doc_x = bow_corpus[document_num]
for i in range(len(bow_doc_x)):
    print("Word {} (\"{}\") appears {} time.".format(
        bow_doc_x[i][0], dictionary[bow_doc_x[i][0]], bow_doc_x[i][1]
    ))

lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics = 2,
    id2word = dictionary, passes = 10, workers = 2)

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic))
    print("\n")