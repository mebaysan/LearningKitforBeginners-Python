import scrapy


class KYSpider(scrapy.Spider):
    name = "kyspider"

    page_count = 0 # sayfa sayısı belirledik next next dedikçe aşağıda if durumu ile kontrol altına alacağız
    file = open("books.txt","a",encoding = "UTF-8")
    book_count=1
    start_urls=[  # standart scrapy yapısını bozduk çünkü bu projede toplu olarak request atmayacağız.
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&page=1" #Başlangıç url'si
    ]

    def parse(self, response):   # standart scrapy yapısını bozduk
        book_names =  response.css("div.name.ellipsis a span::text").extract()  # scrapy shell response ile elde ettiğimiz verileri liste olarak atıyoruz
        book_authors = response.css("div.author span a span::text").extract()   
        book_publishers = response.css("div.publisher span a span::text").extract()

        i = 0
        while(i < len(book_names)):   # basit bir while döngüsü ile durumu kontrol etmeye başladık. len komutu sayesinde her bir sayfada elimize gelen veri kadar işlem yapacak.
            """yield{     #json dosyasına yazmayacağımız için burayı yorum haline aldık.
                "name" : book_names[i],
                "author" : book_authors[i],    # json dosyası olarak yazacağız. yield komutu kullandık ve dictionary formatında yazıyoruz.
                "publisher" : book_publishers[i] # [i] diyerek i'nin o anki değerini aldık.
            }"""
            self.file.write("-------------------------------------------------------------------------------------\n")
            self.file.write(str(self.book_count) + ".\n") # kitap sırasını belirledik
            self.file.write("Kitap İsmi : " + book_names[i] + "\n") # kitap ismini yukardan aldığımız değişkenler ile belirledik
            self.file.write("Yazar : " + book_authors[i] + "\n")
            self.file.write("Kitap Evi : " + book_publishers[i] + "\n")
            self.file.write("-------------------------------------------------\n")
            self.book_count += 1    # kitap sayısını aldık ve 1 arttırdık her seferinde
            i+=1  # döngüyü her seferinde bir arttırdık ki kitap değeri artsın.
        next_url = response.css("a.next::attr(href)").extract_first()  # sonraki url adresine gitmek için kullandığımız scrapy shell
        self.page_count += 1 # yukarda oluşturduğumuz page countu 1 arttırıyoruz her seferinde. self olmasının sebebi oop olması ;)

        if next_url is not None and self.page_count != 5:  # Meali -> next_url varsa ve page_count 5 değilse
            yield scrapy.Request(url = next_url,callback = self.parse)  # yield ile yeni bir request oluşturduk içine parametre olarak yeni url'i yani nex_urli verdik callback parametresi ile hangi fonksiyonu çalıştırmak istediğimizi söyledik.
        else:
            self.file.close()     # sayfa bittiğinde dosyayı kapatacak