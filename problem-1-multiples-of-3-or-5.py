def sum_of_multiples(n):
	multiples_of_3_or_5 = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]
	print(sum(multiples_of_3_or_5))
	
sum_of_multiples(1000)
