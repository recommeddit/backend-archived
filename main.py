#!/usr/bin/python

import sys
import search
import comments
import markdown_to_plaintext


def main():
    # assume first argument is query
    query = sys.argv[1]

    # search google reddit.com CSE for "best <query name>"
    reddit_urls = search.returnlinks(query)
    print(reddit_urls)

    # resolve reddit URLs to comments
    reddit = comments.connect()
    reddit_post_comments = []
    for reddit_url in reddit_urls:
        reddit_post_comments.append(comments.get_comments(reddit, reddit_url))

    # flatten list of lists of comments
    all_comments = [item for sublist in reddit_post_comments for item in sublist]

    # get keys of all_comments
    all_comments = [*all_comments]

    # convert from markdown to plaintext
    all_comments = [markdown_to_plaintext.unmark(comment) for comment in all_comments]

    print(all_comments)


if __name__ == "__main__":
    main()
