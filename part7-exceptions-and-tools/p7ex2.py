#!/usr/bin/env python

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
        oops()
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
