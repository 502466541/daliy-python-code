###############################################################################
# for de_barcode like this type  " P1 NNNNNNATCGCA "  
# author: Han Shaoqing
# Date: 20200217
# analysis for yuanyushu debarcode
# usage:
# 		python de_barcode.py fq1.gz fq2.gz barcode_file.txt
###############################################################################

from sys import argv

file_name = argv[1].split('_')[0]

def read_has_barcode(barcode,read):
	if barcode in read[7:7+len(barcode)]:
		read = read[7+len(barcode):]

		return read

with open(argv[3]) as bf:
	for line in bf:
		
		line = line.strip().split("\t")
		bar = line[1].split("N")[-1]
		barcodes[line[0]] = [gzip.open(str(file_name) + "." + str(line[0]) + ".R1.fq.gz", 'w'),
		gzip.open(str(file_name) + "." + str(line[0]) + ".R2.fq.gz", 'w')]

		with my_open(argv[1],'r') as fastq_file_1, my_open(argv[2],'r') as fastq_file_2:
			while True:
				try:
					name_1 = fastq_file_1.next()
					seq_1 = fastq_file_1.next()
					seq_1_re = read_has_barcode(bar,seq_1)
					fastq_file_1.next()
					plus = "+\n"
					quality_1 = fastq_file_1.next()
					quality_1_re = read_has_barcode(bar,quality_1)

					name_2 = fastq_file_2.next()
					seq_2 = fastq_file_2.next()
					seq_2_re = read_has_barcode(bar,seq_2)
					fastq_file_2.next()
					plus = "+\n"
					quality_2 = fastq_file_2.next()
					quality_2_re = read_has_barcode(bar,quality_2)

					if name_1.split()[0] != name_2.split()[0]:
						print (name_1, name_2)
						raise Exception("Read 1 is not same name as Read 2")

					result_1 = str(name_1) + str(seq_1_re) + str(plus) + str(quality_1_re)
					result_2 = str(name_2) + str(seq_2_re) + str(plus) + str(quality_2_re)

					barcodes[barcode][0].write(result_1)
					barcodes[barcode][1].write(result_2)





