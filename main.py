import spacy
from helpers import *


# load the spacy french model
nlp = spacy.load('fr_core_news_md')

def segment_token(list_of_combinations):
	# initialize a dict of similarity values and resulted token
	sim_values = {}
	separated_tokens = ''
	# loop over the list of cobinations
	for elm in list_of_combinations:
		# split string into three parts by inner space
		text = elm.split(' ')
		token1 = text[0]
		token2 = text[1]
		token3 = text[2]

		# check if the third token is empty so we measure the similarity just between two tokens
		if token3 == '':
			# convert the set of tokens into a scpaCy documents
			token_1_vector = nlp(token1)[0]
			token_2_vector = nlp(token2)[0]
			# check if these two documents objects does have a valid vector
			if token_1_vector.has_vector and token_2_vector.has_vector:
				# we apply the sigmoid to the cosine similarity to move from degree to some sort of probabilities
				sim = sigmoid(token_1_vector.similarity(token_2_vector))
				# set the similarity values into a dictionary as keys and resulted strings as values
				sim_values[sim] = token1+' '+token2
				separated_tokens = sim_values[max(sim_values)]
		else:
			token_1_vector = nlp(token1)[0]
			token_2_vector = nlp(token2)[0]
			token_3_vector = nlp(token3)[0]
			# in this case we have three tokens to separate
			if token_1_vector.has_vector and token_2_vector.has_vector and token_3_vector.has_vector:
				# call measure_similarity function to calculate the cosine similarity between the three generated tokens
				sim = measure_similarity(nlp, token1, token2, token3)
				sim_values[sim] = elm
				separated_tokens = sim_values[max(sim_values)]

	return separated_tokens



if __name__ == '__main__':

	# set a test token
	token = "onveuxbien"

	# generate a list of combinations
	list_of_combinations = generate_combination(token)

	result = segment_token(list_of_combinations)

	print("raw token is {}".format(token))
	print("processed token is {}".format(result))

