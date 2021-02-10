#!/usr/bin/python

import sys
import search
import comments


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


def main():
    query = sys.argv[1]
    reddit_urls = search.returnlinks(query)
    reddit = comments.connect()
    reddit_comments = []
    for reddit_url in reddit_urls:
        reddit_comments.append(comments.get_comments(reddit, reddit_url))
    all_comments = [item for sublist in reddit_comments for item in sublist]
    print(all_comments)


if __name__ == "__main__":
    main()
