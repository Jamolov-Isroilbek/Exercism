def to_rna(dna_strand):
    rna_complement = ''

    for nucleotide in dna_strand:
        if nucleotide == 'G':
            rna_complement += 'C'
        elif nucleotide == 'C':
            rna_complement += 'G'
        elif nucleotide == 'T':
            rna_complement += 'A'
        # elif nucleotide == 'A':
        else:
            rna_complement += 'U'

    return rna_complement