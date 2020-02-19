from sys import argv

f_list=[]
r_list=[]
over_list=[]

def get_list(file_name):
	content = []
	with open(file_name) as k:
		while True:
			try:
				content.append(next(k))
			except StopIteration:
				break

	return content

f_list = get_list(argv[1])
r_list = get_list(argv[2])

over_list = [i for i in f_list if i in r_list]
f_uniqlist = [i for i in f_list if i not in r_list]
r_uniqlist = [i for i in r_list if i not in f_list]

with open ( argv[1]+'_uniq.txt' , 'w') as f:
	for i in f_uniqlist:
		f.write(i)
with open ( argv[2]+'_uniq.txt', 'w') as r:
	for i in r_uniqlist:
		r.write(i)
with open ( argv[1]+argv[2]+'_overlap.txt', 'w') as o:
	for i in over_list:
		o.write(i)
f.close()
r.close()
o.close()
print(argv[1]+" uniq numbers: "+str(len(f_uniqlist))+"\noverlap numbers: "+str(len(over_list))+"\n"+argv[2]+" uniq numbers: "+str(len(r_uniqlist)))
