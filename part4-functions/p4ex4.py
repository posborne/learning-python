#!/usr/bin/env python

def adder(**args):
    """
    Adds up the all the values for the keys in the
    provided dictionary
    """
    res = args[args.keys()[0]]
    for key in args.keys()[1:]:
        res += args[key]
    return res

if __name__ == '__main__':
    print "Testing Adder:"
    print "adder(b=5, c=7):", adder(b=5, c=7)
    print "adder(dogs='cows', b='zebras'): ", adder(dogs='cows', b='zebras')
