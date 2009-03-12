#!/usr/bin/env python
import math

def forSqrt(L):
    """
    Compute the square roots of a list using a for loop
    """
    sqrtlist = []
    for num in L:
        sqrtlist.append(math.sqrt(num))
    return sqrtlist

def mapSqrt(L):
    """
    Compute the square roots of a list using map
    """
    return map(math.sqrt, L)

def lcSqrt(L):
    """
    Compute the square roots of a list using a list comprehension
    """
    return [math.sqrt(x) for x in L]

if __name__ == '__main__':
    squares = [2, 4, 9, 16, 25]
    print "squares:", squares
    print ""
    print "forSqrt(sqares):", forSqrt(squares)
    print "mapSqrt(sqares):", mapSqrt(squares)
    print "lcSqrt(sqares):", lcSqrt(squares)
