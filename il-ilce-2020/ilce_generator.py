import sqlite3
import os
import time

BASEDIR = os.path.abspath(os.path.dirname(__file__))


sqlite_path = os.path.join(BASEDIR, 'db.sqlite3')
sqlite_db = sqlite3.connect(sqlite_path)

sqlite_cursor = sqlite_db.cursor()

sqlite_query = "select * from siparis_il"
sqlite_cursor.execute(sqlite_query)

sehirler = [

]

for i in sqlite_cursor:
    sehirler.append({'id':i[0],'isim':i[1]})

for sehir in sehirler:
    print(sehir)



sayac = 0
with open(BASEDIR+'/ililce.csv',"r",encoding="utf-8") as dosya:
    for satir in dosya:
        if sayac == 0:
            pass
        else:
            sehir = satir.split()[0]
            ilce = satir.split()[1]
            ilce = ilce[1:]
            for sehir_dict in sehirler:
                if sehir == sehir_dict['isim']:
                    try:
                        sqlite_query = "insert into siparis_ilce (il_id,ad) values({},'{}')".format(sehir_dict['id'],ilce)
                        sqlite_cursor.execute(sqlite_query)
                        sqlite_db.commit()
                    except:
                        pass
        sayac+=1

sqlite_db.close()