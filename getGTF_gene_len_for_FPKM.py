################################################################################################
#   Usage:  python get_gene_len.py gencode.v31.annotation.gtf > gencode.v31.gene_length.txt    #
################################################################################################
import HTSeq
import sys, getopt
import os

annotation_file = sys.argv[1]
merge_bedfile = annotation_file + '.merged.bed'
def create_gene_len(annotation_file):
	bedfile = annotation_file + '.unsort.bed'
	sort_bedfile = annotation_file + '.sorted.bed'
	merge_bedfile = annotation_file + '.merged.bed'
	gtf_file = HTSeq.GFF_Reader( annotation_file, end_included=True)
	with open( bedfile, "w") as cleanGTF:
		number_gene = 0
		for feature in gtf_file:
			if feature.type == 'gene':
				number_gene+=1
			if feature.type == 'exon':
				row = [feature.attr['gene_id']+'-'+str(feature.iv.chrom),str(feature.iv.start),str(feature.iv.end),feature.attr['transcript_name'],feature.attr['gene_type'],str(feature.iv.strand)]
				cleanGTF.write('\t'.join(row) + '\n')
		print ("total gene numbers: ",number_gene)
	sort_command = 'sort -k1,1 -k2,2n '+ bedfile +' > ' + sort_bedfile
	os.system(sort_command)

	merge_command = 'bedtools merge -s -c 4,5 -o collapse -delim "|" -i '+sort_bedfile+' > '+merge_bedfile
	os.system(merge_command)

def cal_gene_len(merge_bedfile):
	gene_len = dict()
	with open(merge_bedfile) as f:
		for line in f:
			line = line.strip().split('\t')
			name = str(line[0])
			name_length = int(line[2])-int(line[1])
			if name in gene_len:
				gene_len[name] += name_length
			else:
				gene_len[name] = name_length
		for k,v in gene_len.items():
			
			print(k.split('-')[0]+"\t"+str(v))


create_gene_len(sys.argv[1])
cal_gene_len(merge_bedfile)
