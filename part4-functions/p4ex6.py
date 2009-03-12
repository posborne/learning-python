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

def addDict(dict1, dict2):
    """
    Compute the union of two dictionaries.  Values from the
    first dictionary will be preferred over the second in the
    case of duplicate keys
    """
    unionDict = copyDict(dict1)
    for key in dict2.keys():
        if not key in unionDict.keys():
            unionDict[key] = dict2[key]

    return unionDict

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 4, 'cows': 'moo', 'bob': 'marley'}
        
    print "dict1:", dict1
    print "dict2:", dict2
    print "union:", addDict(dict1, dict2)
