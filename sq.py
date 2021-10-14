
# revers complement sequence
# seq = complement(revers_seq)  
def complement(s):
	basecomplement = {
         "A":"T",
          "T":"A",
          "G":"C",
          "C":"G",
          "a":"t",
          "t":"a",
          "g":"c",
          "c":"g",
			"N":"N",}
	letters = list(s)
	letters = [basecomplement[base] for base in letters]
	letters = letters[::-1]

	return ''.join(letters)
