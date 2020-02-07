"""
Override - Üstüne Yazma (Ezme)
"""


class Animal:
    def to_string(self):
        print("animal")
        
    def walk(self):
        print("animal walking")

class Monkey(Animal):
    def to_string(self):
        print("monkey")


monkey = Monkey()
monkey.walk() # Animal (Parent) Class'ın walk methodunu çalıştırırken
monkey.to_string() # Monkey (Child) Class'ın to_string methodunu çalıştırır