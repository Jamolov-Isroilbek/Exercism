def equilateral(sides):
    if not is_triangular(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_triangular(sides):
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a == b or a == c or b == c


def scalene(sides):
    if not is_triangular(sides):
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a != b and a != c and b != c

def is_triangular(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return (a > 0) and (b > 0) and (c > 0) and (a + b >= c) and (b + c >= a) and (a + c >= b)