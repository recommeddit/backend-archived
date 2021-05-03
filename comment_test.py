import comment_sentiment as c_s
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

def runCommentSentiment():
	exampleComment = "VSCode is my favorite editor. Sublime is also pretty nice. Atom is my least favorite. VSCode has some nice themes\
		and customization options. Atom looks very okay."

	keywords = ['VSCode', 'Atom', 'Sublime']

	print(c_s.getCommentSentiment(exampleComment, keywords, 5))

runCommentSentiment()
