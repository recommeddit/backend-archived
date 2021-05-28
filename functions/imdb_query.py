# importing the module
import imdb
from fuzzywuzzy import fuzz

ia = imdb.IMDb()

THRESHOLD = 90


def cross_reference_imdb(entry):
    # searching the movie
    name, score = entry
    search = ia.search_movie(name)

    # printing the result
    return fuzz.token_set_ratio(name, search[0]) >= THRESHOLD
