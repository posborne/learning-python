#!/usr/bin/env python

class Set(list):
    """
    A class representation of a set along with the associated
    operations.  A set is basically a list without duplicates
    and guarentees about order (though this implementation
    does include such guarentees).
    """

    def __init__(self, value = []):
        self.data = []
        self.concat(value)
        self.index = 0

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:] # a copy of the data
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self

    def next(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 1
        return self.data[self.index - 1]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + `self.data`

    def __add__(self, other):
        return union(other)

class FlexibleSet(Set):
    
    def union(self, *args):
        res = self.data[:]
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return res

    def intersect(self, *args):
        res = []
        for x in self.data:
            for other in args:
                if x in other and x not in res: 
                    res.append(x)
        return res

if __name__ == '__main__':
    # Test intersect and union ops (& |)
    print "== TESTING INTERSECT AND UNION =="
    l1 = [1,2,3]
    l2 = [2,3,4,5]
    s1 = Set(l1)
    s2 = Set(l2)
    print "s1, s2:", s1, ",", s2
    print "s1 & l2:", s1 & l2
    print "s1 | s2:", s1 | s2

    # Test operations with strings
    print "\n== TESTING OPS WITH STRINGS =="
    bobSet = Set('bobby')
    print "bobSet:", bobSet # notice, no duplicates
    print "bobSet[1]:", bobSet[1]
    
    # Iteration
    print "\n== ITERATION TEST =="
    for x in Set('supercalifragilisticespealidocious'):
        print x,
    print ""

    # Operations with strings
    print "\n== OPERATION WITH STRING SETS =="
    print "bobSet & 'mychars':", bobSet & 'mychars'
    print "bobSet | 'mychars':", bobSet | 'mychars'

    # Operations testing multi-args
    print "\n== OPERATION WITH MULTI-ARGS =="
    f1 = FlexibleSet([10,20,30,40])
    l5 = [10, 15, 20]
    l6 = [20, 30, 40]
    l7 = [25, 30, 35]
    print "f1, l5, l6, l7 :", f1, l5, l6, l7
    print "f1.union(l5, l6, l7):", f1.union(l5, l6, l7)
    print "f1.intersect(l5, l6, l7):", f1.intersect(l5, l6, l7)
