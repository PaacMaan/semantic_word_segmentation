from wordseg import segment_token


if __name__ == '__main__':

	# set a test token
	token = "onveuxbien"

	result = segment_token(token)

	print("raw token is {}".format(token))
	print("processed token is {}".format(result))
