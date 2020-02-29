def is_prime(n): 
	if n < 2:
		return False
	if n == 2:
		return True
	for q in range(2, int(n**.5) + 1):
		if not n % q:
			return False
	return True


def main():
	n = input('give me an integer ')
	while type(n) != int:
		try:
			n = int(n)
		except:
			n = input("that's not an integer. give me an integer ")
	ps = f'{n} is '
	if is_prime(n):
		ps += 'prime.'
	else:
		ps += 'not prime.'
	print(ps)


if __name__ == '__main__':
	main()