# converting reviews to list of sentences
# each sentence is a list of words in itself
# essentially, creating a list of lists

import nltk.data;
nltk.download();
from review2wordlist import review2wordlist;

# loading punkt tokenizer for splitting into sentences
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle');

def review2sentences(raw_review,tokenizer,remove_stopwords=False):
	raw_review=raw_review.decode('utf8');
	raw_sentences=tokenizer.tokenize(raw_review.strip()); # creates list of sentences. Each sentence is one entity
							      # not a list of comma separated words
	# looping over each sentence
	sentences=[];
	for sentence in raw_sentences:
		if len(sentence)>0:	
			sentences.append(review2wordlist(sentence,remove_stopwords)); # executes for non-empty sentences 
										      # converts sentence to list of words
	return sentences; # returns a list of wordlists
