for i in range(1,1000000):
	if str(i)[0]==str(i)[-1] and not (i%3 or i%5 or i%7):
		print(i)
