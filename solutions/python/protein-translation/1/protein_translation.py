def proteins(strand):
    rna_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    } 

    result = []
    
    for i in range(0, len(strand), 3):
        single_rna = strand[i : i + 3]
        single_protein = rna_protein[single_rna]
        if single_protein == "STOP":
            break
        result.append(single_protein)
            
    return result
    
