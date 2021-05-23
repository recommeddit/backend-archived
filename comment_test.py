import comment_sentiment as c_s
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

def runCommentSentiment():
	exampleComment = "Infinity War is a better movie imo. It flows better, it’s pacing is better, and feels less disjointed than Endgame. That being said, I enjoyed watching Endgame more, solely because it feels like a comic book come to life. I legitimately got chills during the portals scene, and I’ve never had that happen with another MCU movie. I love both movies, and I fully acknowledge that Infinity War is a better movie, but I enjoyed watching Endgame more and therefore I rank it higher on my personal list."

	keywords = ['Infinity War', 'Endgame']

	print("Keywords: Infinity War, Endgame")
	print("Comment: ", exampleComment)
	print("Reddit Upvotes: 6100")
	print(c_s.get_scores(keywords, exampleComment, 6100))

runCommentSentiment()
