from sys import argv

def merge(intervals):
    '''
    @msg: 合并多个区间
    @param intervals {list} 一个二维数组，每一项代表一个区间
    @return: {list}  返回合并后的区间列表
    '''

    intervals = [sorted(x) for x in intervals]
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
             merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def sum_list(list_val):
	su = 0
	for i in list_val:
		su = su + (int(i[1]) - int(i[0]))
	
	return su

with open (argv[1]) as f:
	gene_interval = []
	gene_name = {}
	raw_name = ''
	for line in f:
		if not line.strip().startswith("#"):
			line = line.strip().split('\t')
			if line[2] == "exon":
				gene_id = line[8].split('\"')[1]
				if gene_id != raw_name:
					gene_interval = []
				gene_interval.append([line[3],line[4]])
				gene_name[gene_id]=gene_interval
				raw_name = gene_id
			else:
				next;

for k,v in gene_name.items():
	intervals = merge(v)
	length = sum_list(intervals)
#	print (k,v)
	print (k,length)
