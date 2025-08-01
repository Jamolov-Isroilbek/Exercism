def sum_of_multiples(limit, multiples):
    combined_set = set()

    for base in multiples:
        if not base:
            continue
        combined_set |= {i for i in range(base, limit, base)}

    return sum(combined_set)