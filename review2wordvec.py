# store a list of of vectors, one per review
# call a function for each review, to average vectors of each word and assign single vector to each paragraph

import numpy as np;

def makeAvgVector(wordlist, model, num_features):
	# function to average all word vectors in a paragraph
	# and assign single vector to each review

	num_of_vectors=0;
	wordset=set(model.wv.index2word); # store list of vocabulary words (not vectors) in a set	
	featureVec=np.zeros((num_features, ),dtype="float32" ); # initialize empty array of size (num_features, ). column matrix

	for word in wordlist:	
		if word in wordset:
			featureVec=np.add(featureVec, model[word]); # add featureVec and vector representation of word given by model[word]
			num_of_vectors+=1;
	
	featureVec=np.divide(featureVec,num_of_vectors); # averaging featureVec sum over number of vectors added
	return featureVec;

def getAvgFeatureVecs(reviewWordlist, model, num_features):
	# function to obtain a list of vectors
	# where each vector is the average word vector for all words in a review
	# each review condensed to an average vector. List of these vectors is returned.

	reviewVecs=np.zeros((len(reviewWordlist), num_features), dtype="float32");
	counter=0; # initialize a counter
	for wordlist in reviewWordlist:
		reviewVecs[counter]= (makeAvgVector(wordlist, model, num_features));
	return reviewVecs;
	
