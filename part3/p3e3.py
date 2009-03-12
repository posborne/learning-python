#!/usr/bin/env python

# Our goal here is to print the items in sorted order
D = {'a': 5, 'cows': 25, 'batman': 22}
keys = D.keys()
keys.sort()
for key in keys:
    print "%s : %i" % (key, D[key])
