from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk.tokenize import TweetTokenizer, sent_tokenize
import nltk

def getCommentSentiment(comment, keywords, upvotes):
	tokenizer_words = TweetTokenizer()
	tokens_sentences = [tokenizer_words.tokenize(t) for t in nltk.sent_tokenize(comment)]
	sentence = ""
	sentenceStruct, sentenceScores, sentimentScores = [], [], []
	sentenceScore = 0
	keywordDetected = False
	for ind in range(0, len(tokens_sentences)):
		keywordDetected = False
		sentenceStruct = tokens_sentences[ind]
		sentence = " ".join(sentenceStruct)
		sentenceScore = sentiment_scores(sentence, upvotes)
		for word in sentenceStruct:
			for keyword in keywords:
				if keywordDetected == False:
					if keyword == word:
						sentenceScores += (keyword, sentenceScore)
						keywordDetected = True
		if keywordDetected == False:
			sentenceScores += ('sentence', sentenceScore)

	finalScores = []
	currKey = 'placeholder'
	currScore = 0.0
	counter = 0
	for ind in range(0, len(sentenceScores)):
		if (type(sentenceScores[ind]) is str) & (sentenceScores[ind] != 'sentence'):
			if currKey == 'placeholder':
				currKey = sentenceScores[ind]
				currScore += sentenceScores[ind+1]
				counter += 1
			elif sentenceScores[ind] != currKey:
				finalScores += (currKey, currScore/counter)
				currKey = sentenceScores[ind]
				currScore = 0.0
				currScore += sentenceScores[ind+1]
				counter = 1
			else:
				currScore += sentenceScores[ind+1]
				counter += 1
		elif sentenceScores[ind] == 'sentence':
			currScore += sentenceScores[ind+1]
			counter += 1
	finalScores += (currKey, currScore/counter)

	return finalScores

def sentiment_scores(sentence, upvotes): 
	sid_obj = SentimentIntensityAnalyzer() 
	sentiment_dict = sid_obj.polarity_scores(sentence)
	pos = sentiment_dict['pos']
	neu = sentiment_dict['neu']
	neg = sentiment_dict['neg']
	score = (2*pos*upvotes) + (neu*upvotes) - (neg*upvotes)
	return score