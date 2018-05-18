# converting reviews to list of words
import re;
from bs4 import BeautifulSoup as bs;
from nltk.corpus import stopwords;

def review2wordlist(raw_review,remove_stopwords=False):

	# for Google's word2vec, input must be in form of sentences
	# also, stopwords may need to be included
	# this function cleans the reviews, removes stopwords if required (does not by default)
	# and returns a list of words from cleaned review

	rev=bs(raw_review).get_text(); 
	rev=re.sub('[^a-zA-Z]',' ',rev);
	wordlist=rev.lower().split();

	if remove_stopwords:
		words=stopwords.words('english');
		wordlist=[w for w in words if not w in stops]; # list of meaningful words i.e. list of review words excluding stopwords
	
	return wordlist;
		
