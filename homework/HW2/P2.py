def dna_complement(dna):
	if dna=='':
		print('DNA string is empty')
		return None
	comp=''
	dna=dna.upper()
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
			return None
	return comp

inputdna='AATGGC'
print('Input DNA is: ',inputdna)
complement=dna_complement(inputdna)
print('Complement DNA is: ',complement)
print('--------------------')
inputdna='TTGCAATTGGCC'
print('Input DNA is: ',inputdna)
complement=dna_complement(inputdna)
print('Complement DNA is: ',complement)
print('--------------------')
inputdna='asdfa'
print('Input DNA is: ',inputdna)
complement=dna_complement(inputdna)
print('Complement DNA is: ',complement)
print('--------------------')
inputdna=''
print('Input DNA is: ',inputdna)
complement=dna_complement(inputdna)
print('Complement DNA is: ',complement)