import comment_sentiment as c_s
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

def runCommentSentiment():
	exampleComment = "I’ve always thought about this as well. Infinity War definitely has a more serious tone and you literally never have a break to process anything. It’s action after action after action. And every time Thanos is on screen, it feels truly terrifying seeing how he’s not a goofy villain. And of course I love how the avengers lose at the end and genuinely feel defeated. With Endgame, it’s definitely more comedic and less serious like Infinity War was. And that’s really weird for me because the way they advertised Endgame was to where it was such a depressing and sad movie. Instead, we overall had a pretty happy movie with many funny moments and the whole time travel aspect being a nostalgic trip for fans. Then of course the ending was cool with every single character we’ve seen all together to battle Thanos and his army. But yeah I agree with you."

	keywords = ['Infinity War', 'Endgame']

	print("Keywords: Infinity War, Endgame")
	print("Comment: ", exampleComment)
	print("Reddit Upvotes: 602")
	print(c_s.get_scores(keywords, exampleComment, 602))

runCommentSentiment()
