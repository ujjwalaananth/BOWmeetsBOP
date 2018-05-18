# cleaning up a review
def review2words(raw_review):
	import re;
	from bs4 import BeautifulSoup as bs;
	from nltk.corpus import stopwords;

	#call this function for all reviews
	
	stops = stopwords.words("english"); #view list of English stop words
	rev=bs(raw_review).get_text(); # removing markup
	rev=re.sub('[^a-zA-z]',' ',rev); # only letters. replace anything ![a-z||A-Z] with ' ' in rev
	words=rev.lower().split(); # convert to lowercase, split into individual words
	meaningful=[w for w in words if not w in stops]; # meaningful is a list of meaningful words i.e. list of review words excluding stopwords
	# creating final review paragraph, meaningful words sep by space
	rev=" ".join(meaningful); # concatenate revised word list into single review paragraph
	return rev; # return cleaned reviews


