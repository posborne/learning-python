#!/usr/bin/env python

class Lister:
    def __repr__(self):
        return ("<Instance of %s(%s), address %s:\n%s>" %
                     (self.__class__.__name__,
                      self.supers(),
                      id(self),
                      self.attrnames()) )

    def attrnames(self):
        result = ''
        for attr in self.__dict__.keys():
            if attr[:2] == '__':
                result += "\tname %s=<built-in>\n" % attr
            else:
                result += "\tname %s=%s\n" % (attr, self.__dict__ [attr])
        return result

    def supers(self):
        result = ""
        first = 1
        for super in self.__class__.__bases__:
            if not first:
                result += ", "
            first = 0
            result += super.__name__
        return result

    
if __name__ == '__main__':
    class Super:
        def __init__(self):               # superclass __init__
            self.data1 = "spam"

    class Sub(Super, Lister):             # mix-in a __repr__
        def __init__(self):               # Lister has access to self
            Super.__init__(self)
            self.data2 = "eggs"           # more instance attrs
            self.data3 = 42

    X = Sub()
    print X            
