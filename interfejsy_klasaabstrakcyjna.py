from abc import ABC, abstractmethod

class Animal:

    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def move(self): pass

    @abstractmethod
    def sleep(self): pass


class Dog(Animal):

    def eat(self): print("Dog eat")

    def move(self): print("Dog move")

    def sleep(self): print("Dog sleep")

d = Dog()
d.eat()