class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller

    def bilgilerigöster(self):
        print("""
        Yazılımcı Objesinin Özellikleri:
        İsim : {}
        Soyisim : {}
        Numara : {} 
        Maaş : {}
        Diller : {}""".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def zamyap(self,zammiktarı):
        print("Zam yapılıyor...")
        self.maaş+= zammiktarı
    def dilekle(self,yenidil):
        print("Dil Ekleniyor...")
        self.diller.append(yenidil)
    def zamazalt(self,zamazalt):
        print("Maaş kısılıyor...")
        self.maaş-=zamazalt
     



yazılımcı1=Yazılımcı("Enes","Baysan",123,3000,["Python"])

yazılımcı1.bilgilerigöster()

yazılımcı1.dilekle("Arapça")
yazılımcı1.bilgilerigöster()

yazılımcı1.zamyap(450)
yazılımcı1.bilgilerigöster()

yazılımcı1.zamazalt(1000)
yazılımcı1.bilgilerigöster()
