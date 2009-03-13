#!/usr/bin/env python

from p6ex2 import MyList

class MySubList(MyList):
    calls = 0 # this is a static variable (all MySubLists)

    def __init__(self, l):
        MyList.__init__(self, l)
        self.adds = 0 # this is an instance variable

    def __add__(self, other):
        MySubList.calls += 1
        self.adds += 1
        return MyList.__add__(self, other)

    def stats(self):
        return self.calls, self.adds
