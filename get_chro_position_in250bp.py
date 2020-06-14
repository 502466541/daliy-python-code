from operator import itemgetter, attrgetter
from sys import argv
num = []
with open(argv[1]) as f:
	for line in f:
		s=[]
		line=line.strip()
		line = line.split("\t")
		s.append(line[0])
		
		s.append(int(line[1]))
		num.append(s)
sort_num = sorted(num, key=itemgetter(0,1))
n = iter(sort_num)
while True:
	try:
		x = next(n)
		y = next(n)
		if x[0] == y[0]:
			if y[1]-x[1] <250:
				print(x,y)
	except StopIteration:
		break
