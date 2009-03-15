#!/usr/bin/env python

class Scene(object):

    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        print "customer:", self.customer.getMessage()
        print "clerk:", self.clerk.getMessage()
        print "parrot:", self.parrot.getMessage()
 
class Customer:
    
    def getMessage(self):
        return "that's one ex-bird"

class Clerk:

    def getMessage(self):
        return "no it isn't..."

class Parrot:
    
    def getMessage(self):
        return "None"

if __name__ == '__main__':
    Scene().action()
