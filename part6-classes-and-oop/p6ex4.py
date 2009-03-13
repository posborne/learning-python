#!/usr/bin/env python

class Meta(object):
    """
    The Meta class has methods which intercept every attribute
    qualification and prints a message with their arguments to
    stdout.
    """
    
    def __getattr__(self, name):
        print name, "requested on Meta"

    def __setattr__(self, name, value):
        print "Attempt to set", name, "to", value
