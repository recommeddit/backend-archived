from MonkeyLearnProductSentiment import *

def get_post(url):
    """
    Get a map of <comments, votes> from post url
    """
    import comments
    reddit = comments.connect()
    comments = comments.get_comments(reddit, url)
    print(comments)
    return comments





    