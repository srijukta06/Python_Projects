def allPrimesUpTo(num):
    primes = [2]
    for number in range(3,num):
        sqrtNum = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                # Not prime
                break
            if factor > sqrtNum:
                # It is prime
                primes.append(number)
                break
    return primes
    pass
