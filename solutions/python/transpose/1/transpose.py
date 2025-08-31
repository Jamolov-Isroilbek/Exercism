def transpose(text):
    lines = text.split("\n")
    rows = len(lines)
    cols = max(len(line) for line in lines)

    result = []
    for c in range(cols):
        row_chars = []
        for r in range(rows):
            if c < len(lines[r]):
                row_chars.append(lines[r][c])
            else:
                row_chars.append(None)  # mark padding explicitly
        # strip only trailing None values
        i = len(row_chars)
        while i > 0 and row_chars[i-1] is None:
            i -= 1
        result.append("".join(ch if ch is not None else " " for ch in row_chars[:i]))

    return "\n".join(result)
