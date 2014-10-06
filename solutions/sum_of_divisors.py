def sum_of_divisors(n):
	sum = 0
	for divisor in range(1,n+1):
		if n % divisor == 0:
			sum += divisor
	return sum
