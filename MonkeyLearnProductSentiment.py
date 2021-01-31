from monkeylearn import MonkeyLearn
#hide api 
import os
from dotenv import load_dotenv
load_dotenv('.env')
api_key = os.getenv('URL_SCRAPE_API_KEY')
################################################################

#temporary using api key, change this to .env later on
ml = MonkeyLearn(URL_SCRAPE_API_KEY)


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
    confidence = "{:.1%}".format(returnMonkey(data)['confidence'])
    #confidence = "{:.1%}".format(0.999)
    return confidence
print(returnConfidence(['laughing out loud']))
