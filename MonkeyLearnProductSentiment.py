from monkeylearn import MonkeyLearn
#hide api 
import os
from dotenv import load_dotenv
load_dotenv('.env')
api_key = os.getenv('URL_SCRAPE_API_KEY')
################################################################

#temporary using api key, change this to .env later on
ml = MonkeyLearn(api_key)


def returnMonkey(data):
    #model id for Product Sentiment
    model_id = 'cl_TWmMTdgQ'
    result = ml.classifiers.classify(model_id, data)

    return result.body[0]['classifications'][0]

#print(returnMonkey(['This is the best IDE']))
def returnPositiveorNot(data):
    #will return either positive neutral or negative
    PositiveorNot = returnMonkey(data)['tag_name']
    return PositiveorNot

#print(returnPositiveorNot(['This is the best IDE']))

def returnConfidence(data):
    #returns confidence in percentage
    confidence = returnMonkey(data)['confidence']
    #confidence = "{:.1%}".format(0.999)
    return confidence
#print(returnConfidence(['laughing out loud']))

################################################################
#seperate data into strings

def seperate_into_strings(text):
    #uses monkeylearn to extract OPINION units from text
    #text is our input, a big reddit comment that may have multiple sentences
    model_id = 'ex_N4aFcea3'
    result = ml.extractors.extract(model_id, text)
    #total is the extractions
    total = result.body[0]['extractions']
    #data is an array of parsed sentences of the original text
    data = []
    for i in range(len(total)):
        data.append(total[i]['extracted_text'])
    return data
'''
print(seperate_into_strings(['The hotel has a great location but all in all it was a horrible experience! \
    Only stayed here because it was the pre-accomodation choice for one of our tours but it was terrible. \
        Will never stay here again!'])[0])
'''
################################################################
#THIS USES THE KEYWORD EXTRACTOR I DON'T KNOW HOW WELL THIS WILL WORKS
#MAY HAVE A PROBLEM WITH DETECTING TOO MANY KEYWORDS
#MAYBE I CAN INCLUDE VALUES WITH A CERTAIN AMOUNT OF RELEVANCE
def keyword_extractor(data):
    model_id = 'ex_YCya9nrn'
    result = ml.extractors.extract(model_id, data)
    array_of_keywords = []
    #total is the extractions
    total = result.body[0]['extractions']
    #appends the top value because I think it automatically sorts by relevance
    for i in range(len(total)):   
        array_of_keywords.append(total[i]['parsed_value'])
    return array_of_keywords

def keyword_extractor_total(data):
    model_id = 'ex_YCya9nrn'
    result = ml.extractors.extract(model_id, data)
    array_of_keywords = []
    #total is the extractions
    total = result.body[0]['extractions']
    
    return total

#print(keyword_extractor(['This error is caused because we try to convert “7.4: to an integer.']))


