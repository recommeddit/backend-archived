# import SentimentIntensityAnalyzer class 
# from vaderSentiment.vaderSentiment module. 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

# function to print sentiments 
# of the sentence. 
def sentiment_scores(sentence): 

	# Create a SentimentIntensityAnalyzer object. 
	sid_obj = SentimentIntensityAnalyzer() 

	# polarity_scores method of SentimentIntensityAnalyzer 
	# oject gives a sentiment dictionary. 
	# which contains pos, neg, neu, and compound scores. 
	sentiment_dict = sid_obj.polarity_scores(sentence) 
	
	print("Overall sentiment dictionary is : ", sentiment_dict) 
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 

	print("Sentence Overall Rated As", end = " ") 

	# decide sentiment as positive, negative and neutral 
	if sentiment_dict['compound'] >= 0.05 : 
		print("Positive") 

	elif sentiment_dict['compound'] <= - 0.05 : 
		print("Negative") 

	else : 
		print("Neutral") 


print("\n1st statement :") 
sentence = "VSCode is pretty good. It can also be kind of bad." 
sentiment_scores(sentence) 

print("\n2nd Statement :") 
sentence = "Atom (after it got a bit of a speed injection) was pretty great (despite the occasional issues with the Squirrel updater eating CPU), \
            but a language plugin I use for work went downhill"
sentiment_scores(sentence) 

print("\n3rd Statement :") 
sentence = "VS Code just got faster/smoother (and I got used to it, as it improved)"
sentiment_scores(sentence) 

print("\n4th statement :") 
sentence = "Sublime is the best overall. It's basically anti-fuck up." 
sentiment_scores(sentence) 

print("\n5th Statement :") 
sentence = "Notepad++ is free and you can set it up to work better than sublime. \
            You may also find yourself needing to add some other things (non-official plugins) to make it do stuff it can't do."
sentiment_scores(sentence) 

print("\n6th Statement :") 
sentence = "Visual Studio is also aaaight."
sentiment_scores(sentence) 

print("\n7th Statement :") 
sentence = "The other Electron based text editors (VS Code, atom.io, etc.) may be flashy and feature packed \
            but the start time for them is horrible if you just want to quickly edit a simple text file. \
            Not to mention the monstrous amount of RAM that they have to use."
sentiment_scores(sentence) 