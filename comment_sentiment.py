from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk.tokenize import TweetTokenizer, sent_tokenize

def getCommentSentiment(comment, keywords, upvotes):
	chunks, keywordSentiments = commentChunk(comment), []
	pos, neg, score = 0.0, 0.0, 0.0
	for ind in range(0, len(chunks)):
		if (ind % 2) == 0:
			pos, neg = sentiment_scores(chunks[ind+1])
			score = (pos*upvotes) - (neg*upvotes)
			keywordSentiments += (chunks[ind], score)

def commentChunk(comment, keywords):
	tokenizer_words = TweetTokenizer()
	tokens_sentences = [tokenizer_words.tokenize(t) for t in nltk.sent_tokenize(comment)]
	keywordChunks = []
	prevKey, currKey, currChunk, sentence = '', '', '', ''
	keywordDetected, runNum = False, 0
	for ind in range(0, len(tokens_sentences)):
		keywordDetected = False
		sentence = tokens_sentences[ind]
		for ell in range(0, len(sentence)):
			currWord = sentence[ell]
			for word in keywords:
				if word == currWord:
					runNum += 1
					keywordDetected = True
					currKey = word
				if keywordDetected == True:
					if runNum == 1:
						prevKey = currKey
						currChunk = currChunk + ' ' + sentence
					else if currKey == prevKey: 
						currChunk = currChunk + ' ' + sentence
					else if currKey != prevKey:
						keywordChunks += (currKey, currChunk)
						prevKey = currKey
						currChunk = ''
					break
			if keywordDetected == True:
				break
			else:
				currChunk = currChunk + ' ' + sentence
				break

	keywordChunks += (currKey, currChunk)

	return keywordChunks

def sentiment_scores(sentence): 
	sid_obj = SentimentIntensityAnalyzer() 
	sentiment_dict = sid_obj.polarity_scores(sentence)
	positivity = sentiment_dict['pos']
	negativity = sentiment_dict['neg']
	return positivity, negativity

