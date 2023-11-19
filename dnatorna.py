def dna_to_rna(dna):
    dna = dna.upper()
    return dna.replace("T","U")

print(dna_to_rna("TTTT"))

