#!/usr/bin/env python

class MyList(list):
    """
    A wrapper around list which does pretty much exactly what a list
    does.
    """
    
    def __init__(self, listval):
        self.listdat = [] # make sure this is a list
        for l in listval: 
            self.listdat.append(l)

    def __add__(self, other):
        return MyList(self.listdat + other)

    def __mul__(self, time):
        return MyList(self.listdat * time)

    def __getitem__(self, index):
        return self.listdat[index]

    def __len__(self):
        return len(self.listdat)

    def __getslice__(self, low, high):
        return MyList(self.listdat[low:high])

    def append(self, node):
        self.listdat.append(node)

    def __getattr__(self, name):
        return getattr(self.listdat, name)

    def __repr__(self):
        return `self.listdat`
    
if __name__ == '__main__':
    x = MyList('somechars')
    print x
    print x[5]
    print x[3:]
    print x + ['cowboys']
    print x * 3
    x.append('bob')
    x.sort()
    for el in x:
        print el,
    
