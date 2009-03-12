#!/usr/bin/env python

def adder(arg1, arg2, *args):
    """
    Adds up the all parameters passed into the function. At least
    two are are required.
    """
    sum = arg1 + arg2
    for arg in args:
        sum += arg
    return sum

if __name__ == '__main__':
    print "Testing Adder:"
    print "adder(1, 2):", adder(1, 2)
    print "adder('a', 'b'):", adder('a', 'b')
    print "adder([1,2], [3,4]):", adder([1,2], [3,4])
    print "adder(1.453, 3.1415926):", adder(1.453, 3.1415926)
    print "adder(1, 2, 3, 4, 5):", adder(1,2,3,4,5)
    print "adder('he', 'is', 'a', 'bird', 'nope'): ", adder('he', 'is', 'a', 'bird', 'nope')
