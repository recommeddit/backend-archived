from MonkeyLearnProductSentiment import *

def get_post(url):
    """
    Get a map of <comments, votes> from post url
    """
    import comments
    reddit = comments.connect()
    comments = comments.get_comments(reddit, url)
    #print(comments)
    return comments

post = get_post("https://www.reddit.com/r/MouseReview/comments/jvvt6e/2020_is_the_year_i_discovered_actually_good_razer/")

#print(post.keys)
#separated_strings = seperate_into_strings(post[)
'''
entities = []
for comment in post.keys():
    doc = seperate_into_strings([comment])

    entities.append(doc)
print(entities)
'''