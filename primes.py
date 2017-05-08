def primes(n):
	prime_list = []
	if n > 1 and isinstance(n,int):
		for num in range(0,n + 1):
		   # prime numbers are greater than 1
		   if num > 1:
		       for i in range(2,num):
		           if (num % i) == 0:
		               break
		       else:
				prime_list.append(num)
		 
		return sorted(prime_list)
	else:
		return " Error: Prime numbers are greater than 1."