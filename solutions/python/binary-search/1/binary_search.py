def find(search_list, value):
    if search_list == []:
        raise ValueError('value not in array')
    return helper(search_list, 0, len(search_list) - 1, value)
    

def helper(search_list, start, end, value):    
    mid_index = (start + end) // 2 
    mid_value = search_list[mid_index]

    if start > end:
        raise ValueError('value not in array')

    if mid_value == value:
        return mid_index
    elif mid_value > value:
        return helper(search_list, start, mid_index - 1, value)
    elif mid_value < value:
        return helper(search_list, mid_index + 1, end, value)

    raise ValueError('value not in array')
