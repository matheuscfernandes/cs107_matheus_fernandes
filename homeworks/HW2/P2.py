def dna_complement(dna):
	comp=''
	for i in dna:
		if i=='A':
			comp=comp+'T'
		elif i=='G':
			comp=comp+'C'
		elif i=='T':
			comp=comp+'A'
		elif i=='C':
			comp=comp+'G'
		else:
			print('{} is not a valit letter'.format(i))
			break
	return comp

inputdna='AATGGC'
print('Input DNA is: ',inputdna)
complement=dna_complement(inputdna)
print('Complement DNA is: ',complement)

