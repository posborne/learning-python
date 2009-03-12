#!/usr/bin/env python

S = 'Arrested development'

print "String: %s\n" % S
print "Character codes:"
for character in S:
    print "%i" % ord(character),

print "\n"
sum = 0
for character in S:
    sum += ord(character)
print "Sum: %i" % sum

print "\nList:"
list = []
for character in S:
    list.append(ord(character))
print list

# A more functional way of doing the same thing
l2 = map(ord, S)
print l2
