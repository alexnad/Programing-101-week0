def nth_fibonacci(n):
	a,b = 1,0
	for i in range(n):
		a,b = a+b,a
	return b




 