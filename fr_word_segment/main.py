from wordseg import segment_token


def main():
	# set a test token
	token = "soitmoinscompliqué"

	# apply segmentation fucntion on the given token
	result = segment_token(token)

	# print raw mispelled token
	print("raw token is {}".format(token))

	# print correct splitted token
	print("processed token is {}".format(result))



if __name__ == '__main__':
	main()
	
