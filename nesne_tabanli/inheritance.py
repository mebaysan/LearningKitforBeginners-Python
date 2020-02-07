"""
Inheritance - Miras / Kalıtım
"""
import chalk
# https://github.com/anthonyalmarza/chalk
# pip install pychalk   -> bu dosyanın çalışması için gerekli (renklendirme modülü)


class Animal: # parent (ebeveyn)
    # __prop  -> private
    # _prop   -> protected
    def __init__(self,**kwargs):
        self.isClimb = kwargs['is_climb']
        self.isFly = kwargs['is_fly']
        self.name = kwargs['name']
        print(chalk.green('Animal is created'))
    
    def is_fly(self):
        if self.isFly == True:
            print(chalk.cyan('{} can fly'.format(self.name)))
        else:
            print(chalk.red("{} can't fly".format(self.name)))

    def is_climb(self):
        if self.isClimb == True:
            print(chalk.cyan('{} can climb'.format(self.name)))
        else:
            print(chalk.red("{} can't climb".format(self.name)))

class Monkey(Animal): # child (çocuk)
    def __init__(self, _is_climb,_is_fly,_name,_foot_count):
        Animal.__init__(self, is_climb=_is_climb,is_fly=_is_fly,name=_name) # parent class'ın __init__ methodunu child class'a aktarmayı sağlar
        self.foot_count = _foot_count
        print(chalk.blue('Monkey is created'))


class Bird(Animal): # child class
    def __init__(self,_is_climb,_is_fly,_name,_wings_count):
        super().__init__(is_climb=_is_climb,name=_name,is_fly=_is_fly) # parent class'ın __init__ methodunu child class'a aktarmayı sağlar
        self.wings_count = _wings_count
        print(chalk.blue('Bird is created'))



maymun = Monkey(True,False,'Goril',2)
kus = Bird(False,True,'Muhabbet Kuşu',2)
maymun.is_fly()
kus.is_fly()
maymun.is_climb()
kus.is_climb()

