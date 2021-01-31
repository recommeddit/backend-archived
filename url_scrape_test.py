#imports
from monkeylearn import MonkeyLearn
import json
import requests

#API Stuff
import os
from dotenv import load_dotenv
load_dotenv('Recommedit.env')
my_api_key = os.getenv('URL_SCRAPE_API_KEY')
url_model_id = 'ex_owGiMc4z'
html_model_id = 'ex_RK5ApHnN'
##############################################################

ml = MonkeyLearn(my_api_key)
comment = ["Go to code.visualstudio.com to get VSCode"]
url_result = ml.extractors.extract(url_model_id, comment)
website = url_result.body[0]["extractions"][0]["extracted_text"]
print(website)

def check_url(sitelink):
    substring = 'https://'
    valid_site = sitelink.find(substring)
    if valid_site == -1:
        sitelink = substring + sitelink   
    return sitelink 

page = requests.get(check_url(website))
html_data = page.content
print(type(html_data))


#TO-DO: convert html data to string and return extracted data

#html_result = ml.extractors.extract(html_model_id, html_data)
#print(html_result.body)