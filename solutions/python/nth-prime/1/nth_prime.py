primes = [2, 3]

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    remaining = number
    
    if len(primes) >= remaining:
        return primes[remaining - 1]
    else:
        remaining -= len(primes)
        
    i = primes[-1]
    while remaining > 0:
        i += 2
        if is_prime(i):
            primes.append(i)
            remaining -= 1
        
    return primes[number - 1]

def is_prime(n):
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    for i in range(5, int(n**0.5) + 1, 6):
        if n % (i + 2) == 0 or n % i == 0:
            return False

    return True