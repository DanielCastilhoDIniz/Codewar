def DNA_strand(dna):
    dna = dna.upper()
    complementar = []
    for letter in dna:
        if letter == "T":
            complementar.append("A")
        if letter == "C":
            complementar.append("G")
        if letter == "G":
            complementar.append("C")
        if letter == "A":
            complementar.append("T")


    return ('').join(complementar)

print(DNA_strand("ATTGC"))


def DNA_strand(dna):
    complementos = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    return ''.join(complementos[letra] for letra in dna.upper())

print(DNA_strand("ATTGC"))


def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))


print(DNA_strand("ATTGC"))