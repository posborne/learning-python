#!/usr/bin/env python

class Animal(object):

    def speak(self):
        print "animal"

    def reply(self):
        self.speak()

class Mammal(Animal):

    def speak(self):
        print "mammal"

class Cat(Mammal):
    
    def speak(self):
        print "meow"

class Dog(Mammal):
    
    def speak(self):
        print "woof"

class Primate(Mammal):
    
    def speak(self):
        print "ooh, ooh, ooh!"

class Hacker(Primate):

    def speak(self):
        print "clickety-clickety"

if __name__ == '__main__':
    a = Animal()
    m = Mammal()
    c = Cat()
    d = Dog()
    p = Primate()
    h = Hacker()

    l = [a,m,c,d,p,h]
    for item in l:
        item.reply()
