import json

from functional import seq

import comments
import recommendations
import search


def dump_comments(query="best C++ IDE", filename="dump.json"):
    # search google for "<query name> reddit"
    reddit_urls = search.return_links(query)

    # resolve reddit URLs to comments and remove HTML/markdown syntax
    # comments are dictionaries of string text, number score, and string url.
    reddit = comments.connect()

    all_comments = (seq(reddit_urls)
                    .flat_map(lambda reddit_url: comments.get_comments(reddit, reddit_url))
                    .map(recommendations.clean_comment))

    with open(filename, 'w') as file_handler:
        json.dump(all_comments.to_list(), file_handler)

    return {"error_message": "", "success": True, "recommendations": all_comments}


def load_comments(filename="dump.json"):
    with open(filename, 'r') as filehandle:
        all_comments = json.load(filehandle)
    return all_comments
