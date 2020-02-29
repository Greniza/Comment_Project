def is_even(x): 
	'''retuns true if x is even, else false'''
	if x % 2:
		return False
	else:
		return True


def main():
	for q in range(11):
		if is_even(q):
			print(f'{q} is even.')
		else:
			print(f'{q} is not even.')


if __name__ == '__main__':
	main()