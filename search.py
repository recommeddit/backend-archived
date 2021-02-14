# from googleapiclient.discovery import build
from apiclient.discovery import build

# the hide api key bs
import os
from dotenv import load_dotenv

load_dotenv(".env")
my_api_key = os.getenv("SEARCH_PY_API_KEY")
cx_key = os.getenv("CX_KEY")
################################################################

resource = build("customsearch", "v1", developerKey=my_api_key).cse()

# search google with string and make sure has reddit in it
# return list of urls with reddit links
# they will do their magic with the reddit links


def returnlinks(searchstring):
    result = resource.list(q="best " + searchstring + " reddit", cx=cx_key).execute()
    linkarray = []
    for item in result["items"]:
        domain = item["displayLink"]
        if domain.endswith("reddit.com"):
            linkarray.append(item["link"])
    return linkarray
