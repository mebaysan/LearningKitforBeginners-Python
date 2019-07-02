
def direct():
    print("Direct çalıştı")

def imported():
    print("import edilerek çalıştı")


if __name__ == "__main__": # eğer dosya direk çalıştırılırsa(ozelMethodlar2.py) bu bloğu çalıştır. python otomatik olarak dosyanın özel değişkenine __name__ "__main__" eşitliyor.
    direct()
else: # eğer dosya direk çağırılmamışsa(mesela başka bir dosyadan kütüphane olarak import edilmişse) bu bloğu çalıştır
    imported()
