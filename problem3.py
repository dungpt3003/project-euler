"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def is_prime(num):
	"""
	Check if a given a number is prime or not

	Test:
	>>> is_prime(2)
	True
	>>> is_prime(1000)
	False
	>>> is_prime(29)
	True
	"""
	if (num <= 3):
		return (num > 1)
	else:
		res = True
		for i in range (2,int(math.sqrt(num)) + 1):
			if (num % i == 0):
				res = False
				break
		return res		


def max_prime_factor(n):
	"""
	Find the largest prime factor of the number n.

	Test:
	>>> max_prime_factor(2)
	2
	>>> max_prime_factor(13195)
	29
	"""
	i = 2
	# Return all prime factor of n
	factors = list()
	while (n > 1):
		while (n % i == 0):
			factors.append(i)
			n = n / i
		i = i + 1
		if (i*i > n):
			if (n > 1):
				factors.append(n)
			break
	# The largest prime factor is factors[-1] 
	# because factors are in increasing order
	return factors[-1]


def main():
	print max_prime_factor(600851475143)


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()

