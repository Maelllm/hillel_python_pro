# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    key = "ACGT"
    dna_2 = ""
    for i in dna:
        dna_2 += key[::-1][key.index(i)]
    return dna_2
