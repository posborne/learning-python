#!/usr/bin/env python

def oops():
    # pass
    # raise KeyError
    raise IndexError

def oopsCaller():
    try:
        oops()
    except IndexError:
        print "Caught an index error"
    except KeyError:
        print "Caught a key error"
    else:
        print "No Exceptions!"

if __name__ == '__main__':
    oopsCaller()
