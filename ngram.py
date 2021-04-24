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