while True:
	x = float(input('Your Integer=> '))
	sc = 0
	while x!=1:
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
