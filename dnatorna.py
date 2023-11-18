def dna_to_rna(dna):
    dna = dna.upper()
    return dna.replace("T","U")

print(dna_to_rna("TTTT"))

a = [1,2,3,4]
b= [ 2*x for x in a]

print(b )
