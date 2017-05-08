def primes(n):
	prime_list = []
	for num in range(0,n + 1):
	   # prime numbers are greater than 1
	   if num > 1:
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
			prime_list.append(num)
	 
	return sorted(prime_list)