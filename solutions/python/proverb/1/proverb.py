def proverb(*words, qualifier=""):
    if not words:
        return []
    
    lines = []
    
    for i in range(len(words) - 1):
        lines.append(f"For want of a {words[i]} the {words[i + 1]} was lost.")
    
    qualifier_prefix = f"{qualifier} " if qualifier else ""
    lines.append(f"And all for the want of a {qualifier_prefix}{words[0]}.")
    
    return lines