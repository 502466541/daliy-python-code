import pandas as pd
import os
import pysam
import sys


# usage:
# python bam2coverage.py bamfile posfile output
#
# bamfile:
# posfile: column1, chrom; column2, position
# output:
#
# position is starting with 1

bamfile = sys.argv[1]
posfile = sys.argv[2]
outfile = sys.argv[3]

def bam2matrix_single_cpu(bam, position, outfile):
	tb_out = pd.DataFrame(columns=['chrom', 'pos', 'A', 'T', 'C', 'G', 'coverage'])
	samfile = pysam.AlignmentFile(bam, "rb")
	for idx, row in position.iterrows():
		bases = {"A": 0, "G": 0, "C": 0, "T": 0}
		chrom_ = row[0]
		pos_a = row[1] - 1
		pos_b = row[1]
		for pileupcolumn in samfile.pileup(chrom_, pos_a, pos_b, truncate=True):
			for pileupread in [al for al in pileupcolumn.pileups if al.alignment.mapq > 26]:
				if not pileupread.is_del and not pileupread.is_refskip:
					base = pileupread.alignment.query_sequence[pileupread.query_position]
					try:
						bases[base] += 1
					except:
						pass
		cov = sum(list(bases.values()))
		tb_out = tb_out.append({
			'chrom': chrom_,
			'pos': row[1],
			'A': int(bases['A']),
			'T': bases['T'],
			'G': bases['G'],
			'C': bases['C'],
			'coverage': cov
		}, ignore_index=True)
	samfile.close()
	tb_out.to_csv(outfile, index=False, sep='\t')

position = pd.read_table(posfile)

bam2matrix_single_cpu(bam=bamfile,position=position,outfile=outfile)
