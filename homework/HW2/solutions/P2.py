def dna_complement(seq):
    '''Compute the complement using a dictionary. Could also use a 
    if loop or map function'''
    
    mapping = {
         "A" : "T", 
         "T" : "A", 
         "G" : "C", 
         "C" : "G"
        }
    res_string = ""
    for s in seq:
        comp = mapping.get(s.upper(), None)
        if(comp == None):
            return None
        res_string += comp
    return(res_string)

# Demo a few strings 
in1 = "ATCGGAatT"
out1 = dna_complement(in1)
print("For input %s the output is %s" % (in1, out1))
in2 = "ABc"
out2 = dna_complement(in2)
print("For input %s the output is %s " % (in2, out2))