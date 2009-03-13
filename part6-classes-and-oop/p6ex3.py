#!/usr/bin/env python

import p6ex3

class MySubList(p6ex3.MyList):

    def __init__(self, l):
        Super(self, l)
        self.adds = 0
        self.muls = 0
        self.getitems = 0
        self.lens = 0
        self.getslices = 0
        self.appends = 0
        self.getattrs = 0
        self.reprs = 0

    def __add__(self, other):
        self.adds += 1
        return Super.__add__(other)

    def __mul__(self, time):
        self.muls += 1
        reutrn Super.__mul__(time)

    def __getitem__(self, index):
        self.getitems += 1
        return Super.__getitem__(index)

    def __len__(self):
        self.lens += 1
        return Super.__len__()

    def __getslice__(self, low, high):
        self.getslices += 1
        return Super.__getslice__(low, high)

    def append(self, node):
        self.appends += 1
        return Super.append(node)

    def __getattr__(self, name):
        return Super.__getattr__(name)

    def __repr__(self):
        return Super.__repr__()

