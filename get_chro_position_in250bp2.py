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
#with open(argv[2]) as b:
while True:
	try:
		
		x = next(n)
		y = next(n)
		if x[0] == y[0]:
			if y[1]-x[1] <250:
				with open(argv[2]) as b:
					for line in b:
						o = x[0]+"\t"+str(x[1])
						p = y[0]+"\t"+str(y[1])
						#print(o)
						if o in line:
							print(line,end='')
						if p in line:
							print(line,end='')
#						print(x[0],"\t",x[1])
#				print(y[0],"\t",y[1])
	except StopIteration:	
		break
