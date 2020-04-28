import sqlite3
import os
import time

BASEDIR = os.path.abspath(os.path.dirname(__file__))


sqlite_path = os.path.join(BASEDIR, 'db.sqlite3')
sqlite_db = sqlite3.connect(sqlite_path)

sqlite_cursor = sqlite_db.cursor()


sayac = 0
with open(BASEDIR+'/ililce.csv',"r",encoding="utf-8") as dosya:
    for satir in dosya:
        if sayac == 0:
            pass
        else:
            sehir = satir.split()[0]
            try:
                sqlite_query = "insert into siparis_il (ad) values('{}')".format(sehir)
                sqlite_cursor.execute(sqlite_query)
                sqlite_db.commit()
                print('ok')
            except:
                print('error')
        sayac+=1

sqlite_db.close()