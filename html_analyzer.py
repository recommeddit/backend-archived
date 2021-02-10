#imports
import url_to_html as urlEx
import json
import nltk
import truecase

##############################################################

redditComment = "code.visualstudio.com is the best code editor"
commentUrl = urlEx.get_url(redditComment)
resolvedUrl = urlEx.check_url(commentUrl)
parsedHtml = urlEx.html_to_text(resolvedUrl)

keywords = []
for par in range(0,len(parsedHtml)):
	data = parsedHtml[par]
	text_to_tag = nltk.word_tokenize(truecase.get_true_case(data))
	tagged = nltk.pos_tag(text_to_tag)
	for ell in range(0, len(tagged)):
		keywords.append(tagged[ell])

#get rid of nltk test and implement spaCy ner