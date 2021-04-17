import comment_sentiment as c_s
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

def runCommentSentiment():
	exampleComment = "VSCode is my favorite editor besides Atom and Sublime. It has a really nice interface as well as a built-in terminal. Also, it has colorful themes \
		and source control. Atom is decent but it's too simple. It's too basic and doesn't have that many \
			features. Sublime is cool and has a similar interface to VSCode. It is very popular amongst programmers."

	keywords = ['VSCode', 'Atom', 'Sublime']

	print(c_s.getCommentSentiment(exampleComment, keywords, 5))

runCommentSentiment()
