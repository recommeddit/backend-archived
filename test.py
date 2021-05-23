import random as rd

titles = ["Eternal Sunshine of the Spotless Mind", "The Mandalorian"]

def simplify_title(titles):
	keywords = []
	titleReferences = []
	simplified = False
	commonWords = 'The the This this Is is A a Of of Into into For for But but And and So so There there Through through As as Like like He he She she They they Them them It it'
	for ind in range(0, len(titles)):
		simplified = False
		title = titles[ind].split()
		while(simplified == False):
			keyword = title[rd.randint(0,(len(title)-1))]
			if keyword not in commonWords:
				simplified = True
				keywords += [keyword]
		titleReferences += (titles[ind], keyword)
	return keywords,titleReferences

keys, fullList = simplify_title(titles)
print(keys)
print(fullList)