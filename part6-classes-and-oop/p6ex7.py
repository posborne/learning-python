#!/usr/bin/env python

class Lunch(object):

    def __init__(self):
        self.cust = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.cust.placeOrder(foodName, self.employee)

    def result(self):
        self.cust.printFood()

class Customer(object):

    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)

    def printFood(self):
        print self.food
        
class Employee(object):

    def takeOrder(self, foodName):
        return Food(foodName)        

class Food(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    l = Lunch()
    l.order("Burritos")
    l.result()
