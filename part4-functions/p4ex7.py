#!/usr/bin/env python

def f1(a, b): print a, b           # normal args

def f2(a, *b): print a, b          # positional varargs

def f3(a, **b): print a, b         # keyword varargs

def f4(a, *b, **c): print a, b, c  # Mixed modes

def f5(a, b=2, c=3): print a, b, c # Defaults

def f6(a, b=2, *c): print a, b, c  # Defaults and positional varargs

#########################################################
# Intereactive output
########################################################
# >>> from p4ex7 import *
# >>> f1(1,2)
# 1 2
# >>> f1(b=2,a=1)
# 1 2
# >>> 
# >>> f2(1,2,3)
# 1 (2, 3)
# >>> f3(1,x=2, y=3)
# 1 {'y': 3, 'x': 2}
# >>> f4(1,2,3,x=2,y=3)
# 1 (2, 3) {'y': 3, 'x': 2}
# >>> f5(1)
# 1 2 3
# >>> f5(1,4)
# 1 4 3
# >>> f6(1)
# 1 2 ()
# >>> f5(1,3,4)
# 1 3 4
# >>> f6(1,3,4)
# 1 3 (4,)
