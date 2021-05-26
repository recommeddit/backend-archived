import html

from functional import seq

import MonkeyLearnProductSentiment
import comments
import dump_comments
import markdown_to_plaintext
import search
from comment import Comment, CommentList


def clean_comment(comment):
    comment["text"] = markdown_to_plaintext.unmark(html.unescape(comment["text"]))
    return comment


def get_recommendations(query):
    if not query:
        return {"error_message": "No query", "success": False, "recommendations": []}

    # search google for "<query name> reddit"
    reddit_urls = search.return_links(query)

    # resolve reddit URLs to comments and remove HTML/markdown syntax
    # comments are dictionaries of string text, number score, and string url.
    reddit = comments.connect()

    all_comments = dump_comments.load_comments("dump.json")

    # chunked_comments = CommentList(
    #     seq(all_comments)
    #         .map(Comment.from_dict)
    #         .to_list()
    # ).chunk()

    chunked_comments = CommentList(
        seq(reddit_urls)
            .flat_map(lambda reddit_url: comments.get_comments(reddit, reddit_url))
            .map(clean_comment)
            .map(Comment.from_dict)
            .to_list()
    ).chunk()

    results = MonkeyLearnProductSentiment.keyword_extractor_chunked(chunked_comments)
    recommendations = seq(results.items()).smap(lambda keyword, score: {"keyword": keyword, "score": score})

    return {"error_message": "", "success": True, "recommendations": recommendations}
