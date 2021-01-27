import nltk
import truecase

sentence = 'michael jackson AnD His Dog like To eat At mcDonalds'
text_to_tag = nltk.word_tokenize(truecase.get_true_case(sentence))

print(nltk.pos_tag(text_to_tag))
