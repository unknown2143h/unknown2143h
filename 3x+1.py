while True:
	x = float(input('Your Integer=> ')) 

## I've used float as the type because the limit of the value of the integer type is too low. but you should put only integers.##

	sc = 0
	while x!=1 and x!= -17 and x != -1 and x != -5:
		if x%2 == 0:
			sc += 1
			x/=2
			print(x)
		else:
			x = 3*x +1
			print(x)
			sc += 1
	if x == 1:
		print(f"Step Count: {sc}")
