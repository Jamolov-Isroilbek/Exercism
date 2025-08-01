def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    
    sum_of_nums = sum(i for i in range(1, number//2 + 1) if number % i == 0)
    if sum_of_nums < number:
        return 'deficient'
    if sum_of_nums > number:
        return 'abundant'
    return 'perfect'