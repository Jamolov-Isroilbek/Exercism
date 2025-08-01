def flatten(iterable):
    result = []

    def helper(iterable, result):
        for i in iterable:
            if i is None:
                continue
            if isinstance(i, list):
                result = helper(i, result)
            else:
                result.append(i)
        return result

    if iterable is not None:
        return helper(iterable, result)
    
    return result
    