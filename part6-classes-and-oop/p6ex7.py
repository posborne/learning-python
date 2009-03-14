#!/usr/bin/env python

class Lunch(object):

    def __init__(self):
        self.cust = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.cust.placeOrder(foodName, self.employee)

    def result(self):
        

class Customer(object):

    def __init__(self):

    def placeOrder(self, foodName, employee):
        

    def printFood(self):

class Employee(object):

    def takeOrder(self, foodName):
        

class Food(object):

    def __init__(self, name):
        self.name = name

