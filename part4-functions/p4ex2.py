#!/usr/bin/env python

def adder(a, b):
    " adds up the two parameters passed to it "
    return a + b

if __name__ == '__main__':
    print "Testing Adder:"
    print "adder(1, 2):", adder(1, 2)
    print "adder('a', 'b'):", adder('a', 'b')
    print "adder([1,2], [3,4]):", adder([1,2], [3,4])
    print "adder(1.453, 3.1415926):", adder(1.453, 3.1415926)
    
