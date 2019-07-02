class Fruits():
    def __init__(self,name,calories): # bu sınıf initialize olduğunda yani türetildiğinde içine gelen parametreler bu sınıfın attribute'ları olacak
        self.name = name
        self.calories = calories

    def __str__(self): # bu sınıf türetildiğinde instance.name demeden bize bu sınıfın name'ini döndürür(burada öyle yazdığımız için bkz. 15. satır)
        return self.name

    def __len__(self): # bu sınıf türetildiğinde instance.calories demeden bize bu sınıfın calories'ini döndürür(burada öyle yazdığımız için bkz. 16. satır)
        return self.calories

    

fruit = Fruits("banana",300)
print(fruit)
print(len(fruit))




# daha detaylı bilgi için google'da arama yapabilirsiniz. Diğer özel methodlara daha rahat ulaşırsınız