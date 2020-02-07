"""
Initializer - Constructor
"""

class Hayvan():
    def __init__(self,_ad,_yas): # bu class oluşurken _ad ve _yas adında birer parametre alacak
        self.ad = _ad # bu class'tan oluşan instance'in ad prop'u _ad'a eşit olacak...
        self.yas = _yas
        print("Instance oluşuyor")
    def get_age(self): # bu class'tan oluşan instance'in methodu
        return self.yas # instance'in kendi adını döndürecek
    


a = Hayvan('Köpek',3)
