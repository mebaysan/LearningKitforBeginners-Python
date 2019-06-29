import sqlite3

conn = sqlite3.connect("database/chinook.db")

cursor = conn.cursor()

cursor.execute(" select FirstName,LastName from customers where city like '%a%' ") # city'sinde 'a' geçenleri al ve FirstName'e göre alfabetik tersten sırala. (a% -> FirstName 'a' ile başlayanlar. %a% -> FirstName'i 'a' içerenler. %a -> FirstName 'a' ile bitenler.) 

for data in cursor:
    print("İsim = {}\nSoyisim = {}\n-------".format(data[0],data[1]))
    