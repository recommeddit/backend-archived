import html
from functional import seq
import search
import comments
import markdown_to_plaintext
import MonkeyLearnProductSentiment


MAX_CHARS = 42000


def get_recommendations(query):
    # search google for "best <query name> reddit"
    reddit_urls = search.returnlinks(query)

    # resolve reddit URLs to comments and remove HTML/markdown syntax
    reddit = comments.connect()
    all_comments = (
        seq(reddit_urls)
        .flat_map(lambda reddit_url: comments.get_comments(reddit, reddit_url))
        .map(html.unescape)
        .map(markdown_to_plaintext.unmark)
    )

    chunked_all_comments = []
    for comment in all_comments:
        if not chunked_all_comments:
            chunked_all_comments.append(comment)
        else:
            newline_and_comment = "\n\n" + comment
            if len(chunked_all_comments[-1] + newline_and_comment) > MAX_CHARS:
                chunked_all_comments.append(comment)
            else:
                chunked_all_comments[-1] += newline_and_comment

    results = dict(
        sorted(
            MonkeyLearnProductSentiment.keyword_extractor_total(
                chunked_all_comments
            ).items(),
            key=lambda item: item[1],
        )
    )
    return results
