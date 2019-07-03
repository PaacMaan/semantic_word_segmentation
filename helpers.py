import math


def average(number1, number2, number3):
	"""
	Calculating the average of three given numbers

	Parameters:
	number1|2|3 (float): three given numbers

	Returns:
	number (float): Returning the statistical average of these three numbers
	"""
	return (number1 + number2 + number3) / 3.0



def measure_similarity(nlp, token_1, token_2, token_3):
	"""
	Measuring the semantic similarity between three tokens

	Parameters:
	token_1|2|3 (string): three given tokens

	Returns:
	number (float): Returning the average of cosine similarity after applying sigmoid
	"""

	token_1_vector, token_2_vector, token_3_vector = nlp(token_1)[0], nlp(token_2)[0], nlp(token_3)[0]

	# initiliazing the average with zero
	avg = 0.0

	# checking if each token does have a valid vector
	if token_1_vector.has_vector and token_2_vector.has_vector and token_3_vector.has_vector:
		# measuring the similarity between each combination of these three tokens
	    similarity_1 = sigmoid(token_1_vector.similarity(token_2_vector))
	    similarity_2 = sigmoid(token_2_vector.similarity(token_3_vector))
	    similarity_3 = sigmoid(token_1_vector.similarity(token_3_vector))
	    similarity_3 = 0
	    # measuring the average of 
	    avg = average(similarity_1, similarity_2, similarity_3)

	return avg


def sigmoid(x):
	"""
	Calculating the sigmoid of a given number

	Parameters:
	x (float): a cosine similarity

	Returns:
	sigmoid (float): Transforming a given cosine similarity to a sort of probability between 0 and 1
	"""
	return 1 / (1 + math.exp(-x))


def generate_combination(token):
	"""
	Generate all possible combination of a three words splitted token

	Parameters:
	token (string): the mispelled word to split

	Returns:
	list_of_combinations (list): a list of all possible combinations that could be extracted from that toekn 
	"""

	# get token's length
	token_length = len(token)

	# initilaise the list_of_combinations
	list_of_combinations = []

	for i in range(0, token_length-1):
	    # build all the possible combinations
	    token_1 = token[0:i+1]
	    token_2 = token[i+1:]
	    for j in range(0, len(token_2)):
	        list_of_combinations.append(token_1+' '+token_2[0:j+1]+' '+token_2[j+1:])

	return list_of_combinations

