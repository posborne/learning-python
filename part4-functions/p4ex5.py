#!/usr/bin/env python

def copyDict(dictionary):
    """
    Create a copy of the dictionary passed into the function.  This
    is a shallow copy so only references of underlying elements are
    copied.
    """
    newdict = {}
    for key in dictionary.keys():
        newdict[key] = dictionary[key]
    
    return newdict

if __name__ == '__main__':
    mydict = {'cows': 'moo', 'dogs': 'woof', 'python': 'pssss'}
    newdict = copyDict(mydict)
    print "mydict  =>", mydict
    print "newdict =>", newdict
