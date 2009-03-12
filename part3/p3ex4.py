#!/usr/bin/env python

L = map(lambda x: 2 ** x, range(7))
X = 5

if 2 ** X in L:
    print 'at index', L.index(2 ** X)
else:
    print X, 'not found'


