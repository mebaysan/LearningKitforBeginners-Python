"""
Abstract Class - Parent Class, Child Class'lar için Şablon görevi görür
Abstract class'lar initialize edilemez
"""
from abc import ABC,abstractmethod

class Animal(ABC): # ABC'den inherit ettik fakat Abstract class'lardan bir instance oluşturulamaz
    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass



class Bird(Animal):
    def __init__(self):
        print("bird is created")
    def walk(self): # abstract class'ın abstractmethod'larını override etmek zorundayız
        print("walk")
    def run(self):
        print("run")


bird = Bird()