def square_root(number): 
    return helper(number, 1, number)


def helper(number, start, end):
    if start > end:
        return end
        
    mid = (start + end) // 2
    multiplier = mid * mid
    
    if number == multiplier:
        return mid
    if number < multiplier:
        return helper(number, start, mid - 1)
    if number > multiplier:
        return helper(number, mid + 1, end)