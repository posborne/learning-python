#!/usr/bin/env python

class Adder:
    def add(self, x, y):
        print "Not Implemented"

class ListAdder(Adder):

    def __init__(self, data):
        self.data = data
    
    def add(self, other):
        """
        Add this list to another
        """
        return self.data + other

    def __add__(self, other):
        return self.add(other)

class DictAdder(Adder):
    
    def __init__(self, value):
        self.data = value

    def add(self, other):
        """
        Do a union of two dictionaries preferring the values of duplicate keys
        from this dictionary
        """
        uniondict = {}
        for key in self.data.keys():
            uniondict[key] = self.data[key]

        for key in other:
            if key not in uniondict.keys():
                uniondict[key] = other[key]
        return uniondict

    def __add__(self, other):
        return self.add(other)
