###############################################################################
# for de_barcode like this type  " P1 NNNNNNATCGCA "  
# author: Han Shaoqing
# Date: 20200217
# analysis for yuanyushu debarcode
# usage:
# 		python de_barcode.py fq1.gz fq2.gz barcode_file.txt
###############################################################################

from os.path import basename
from sys import argv
import gzip
file_name = basename(argv[1]).split('_')[0]

def reformat_read(name_1, seq_1, plus_1, quality_1,name_2, seq_2, plus_2, quality_2,barcode):
	name_1 = str(name_1,'utf-8')
	seq_1 = str(seq_1,'utf-8')
	quality_1 = str(quality_1,'utf-8')
	
	name_2 = str(name_2,'utf-8')
	seq_2 = str(seq_2,'utf-8')
	quality_2 = str(quality_2,'utf-8')

	
	if barcode == seq_1[6:12]:
		seq_1 = seq_1[12:]
		quality_1 = quality_1[12:]

		result1 = name_1 + seq_1 + plus_1 + quality_1
		result2 = name_2 + seq_2 + plus_2 + quality_2
	else:
		result1 = ''
		result2 = ''

	return result1, result2

with open(argv[3]) as bf:
	for line in bf:
		barcodes = {}
		line = line.strip().split("\t")
		bar = line[1]
		bar_name = line[0]
		barcodes[line[0]] = [gzip.open(str(file_name) + "." + str(line[0]) + ".R1.fq.gz", 'w'),gzip.open(str(file_name) + "." + str(line[0]) + ".R2.fq.gz", 'w')]

		with gzip.open(argv[1]) as fastq_file_1, gzip.open(argv[2]) as fastq_file_2:
			while True:
				try:
					name_1 = next(fastq_file_1)
					seq_1 = next(fastq_file_1)
					next(fastq_file_1)
					plus_1 = "+\n"
					quality_1 = next(fastq_file_1)

					name_2 = next(fastq_file_2)
					seq_2 = next(fastq_file_2)
					plus_2 = "+\n"
					next(fastq_file_2)
					quality_2 = next(fastq_file_2)
					result_1, result_2 = reformat_read(name_1, seq_1, plus_1, quality_1,name_2, seq_2, plus_2, quality_2,bar)
					
					result_1 = result_1.encode('utf-8')
					result_2 = result_2.encode('utf-8')
					barcodes[line[0]][0].write(result_1)
					barcodes[line[0]][1].write(result_2)
				except StopIteration:
					break

fastq_file_1.close()
fastq_file_2.close()
bf.close()
