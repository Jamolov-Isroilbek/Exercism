def find_anagrams(word, candidates):
    freq_map = {}
    anagrams = []

    for i in word.lower():
        freq_map[i] = freq_map.get(i, 0) + 1
    
    for i in candidates:
        candidate_freq_map = {}
        
        for j in i.lower():
            candidate_freq_map[j] = candidate_freq_map.get(j, 0) + 1
            
        if freq_map == candidate_freq_map and word.lower() != i.lower():
            anagrams.append(i)

    return anagrams