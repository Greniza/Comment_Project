import prime

def main():
	maxnum = 'a'
	while type(maxnum) != int:
		maxnum = input("give me a number that's greater than or equal to 2\n")
		try:
			maxnum = int(maxnum)
			if maxnum < 2:
				maxnum = 'a'
		except:
			print("that is not a number")
	for x in range(2, maxnum + 1):
		if prime.is_prime(x):
			print(x, end = ', ')


if __name__ == '__main__':
	main()