#!/usr/bin/env python

def safeCall(func, *args):
    import sys, traceback
    """
    Call any function safely* with safeCall.  Functions run in
    safeCall will simply print out exceptions when they happen
    rather than dying.
    """
    try:
        apply(func, args)
    except:
        traceback.print_exc()
        print 'Got', sys.exc_type, sys.exc_value

# Let's use this safecall

class MyError:
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return "That's my error:", self.message

def oops():
    # pass
    # raise KeyError
    # raise IndexError
    raise MyError, "Yeah, that's not good"

def oopsCaller():
    try:
        safeCall(oops)
    except IndexError:
        print "Caught an index error"
    except KeyError:
        print "Caught a key error"
    except MyError, X:
        print "Caught MyError:", X.message
    else:
        print "No Exceptions!"

if __name__ == '__main__':
    oopsCaller()

