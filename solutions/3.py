f=open('inputs/3.txt')
for t in range(int(f.readline())):
	L,k=[int(x) for x in f.readline().split()],int(f.readline())
	print(sorted(L)[len(L)-k])