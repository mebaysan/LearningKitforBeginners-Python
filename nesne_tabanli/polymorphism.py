"""
Polymorphism - Çok Biçimlilik
Parent Class'tan Child(Sub) Class'a aktarılan; fakat Child Class'ta farklı biçimde kullanılan 
methodlar varsa bu olaya polymorphism denir
"""


class Employee:
    def __init__(self, _salary):
        self.salary = _salary

    def increase(self): # aynı methodu sub class'larda farklı 'BİÇİMDE' kullandık (increase_rate)
        increase_rate = 0.1
        self.salary = self.salary + (100 * increase_rate)


class SoftwareDeveloper(Employee):
    def __init__(self, _salary):
        super().__init__(_salary)

    def increase(self):
        increase_rate = 0.2 # Parent Class'tan aldığımız methodu farklı 'BİÇİMDE' kullandık (increase_rate)
        self.salary = self.salary + (100 * increase_rate)


class BlueCollar(Employee):
    def __init__(self, _salary):
        super().__init__(_salary)

    def increase(self):
        increase_rate = -0.1
        self.salary = self.salary + (100 * increase_rate)


developer = SoftwareDeveloper(1000)
blue_collar = BlueCollar(1000)
developer.increase()
blue_collar.increase()
print(developer.salary)
print(blue_collar.salary)
