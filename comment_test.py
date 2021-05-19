import comment_sentiment as c_s
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

def runCommentSentiment():
	exampleComment = "VSCode is built from the ground up, focusing on customization, extension. What's more, its open source and it's microsoft! Huge existing microsoft products and the growth rate of new VSCode community keeps increasing. The product development is only very fast! At this pace of product development, community growth, extensions growth, I can't imagine other editors like Sublime and Atom can keep it up." 

	keywords = ['Sublime', 'VSCode']

	print("Keywords: Sublime, VSCode")
	print("Comment: ", exampleComment)
	print("Reddit Upvotes: 3")
	print(c_s.getCommentSentiment(exampleComment, keywords, 3))

runCommentSentiment()
