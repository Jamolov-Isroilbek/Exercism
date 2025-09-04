def saddle_points(matrix): 
    res = []

    if len({len(r) for r in matrix}) > 1:
        raise ValueError("irregular matrix")
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            curr = matrix[row][col]

            max_row = max(matrix[row])
            min_col = min(r[col] for r in matrix)            

            if max_row == min_col == curr:
                res.append({"row": row + 1, "column": col + 1})

    return res