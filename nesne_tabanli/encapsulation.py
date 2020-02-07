"""
Encapsulation - Method veya Property'lere erişimleri kısıtlama
"""
import chalk
# https://github.com/anthonyalmarza/chalk
# pip install pychalk   -> bu dosyanın çalışması için gerekli (renklendirme modülü)
class BankAccount:
    def __init__(self,_name,_money,_addres):
        self.name = _name           # global
        self.__money = _money       # private (__attr_name)
        self.address = _addres
    # Get & Set
    def get_money(self):
        return self.__money # bu instance'in __money attr'ini döner

    def set_money(self,_money):
        self.__money = _money # bu instance'in __money attr'ini set eder

    def increase_money(self): # private attr'i farklı bir şekilde set ettik. Aynı şekilde bu methodu da private (__method_name) yapabilirdik. Sadece sınıf içerisinden kullanabilirdik
        self.__money+=500

    def get_props(self):
        return """
            Name    : {}\n
            Money   : {}\n
            Address : {}
        """.format(self.name,self.get_money(),self.address)

person = BankAccount("Baysan",3000,"İstanbul")
print(chalk.green(person.get_props()))
person.set_money(3500)
print(chalk.blue(person.get_props()))
person.increase_money()
print(chalk.red(person.get_props()))