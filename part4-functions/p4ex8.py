#!/usr/bin/env python

def isPrime(num):
    if (num <= 1):
        return False
    x = num // 2
    while x > 1:
        if num % x == 0:
            return False
        x -= 1
    return True # It is prime

if __name__ == '__main__':
    # find all primes between 1 and 1000
    primes = []
    for num in range(1000):
        if (isPrime(num)):
            primes.append(num)

    print "There are", len(primes), "primes between 1 and 1000"
    print "Here they are: ", primes
