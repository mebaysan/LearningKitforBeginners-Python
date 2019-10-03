from django.db import models


class Blog(models.Model):  # her model bir tabloya denk gelir. Buradaki 'Blog' aslında bizim tablomuzdur.
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık',
                             help_text='Başlık Bilgisi Burada Girilir')
    # CharField -> karakter alanı , max_length -> Max karakter uzunluğu zorunludur, verbose_name -> Formda nasıl gözükeceği, help_text -> Formun altında bilgi olarak gözükecek metin, blank -> formda boş girilip girilmemesi, null -> veritabanına boş kayıt edilip edilememesi
    content = models.TextField(max_length=1000, verbose_name='İçerik', null=True, blank=False)
    created_date = models.DateField(auto_now_add=True,
                                    auto_now=False)  # auto_now_add -> oluşturulma tarihini otomatik ekler, auto_now -> Bu nesne her değişime uğradığında otomatik olarak created_date'i güncellenir

    class Meta: # bu class altına bu modelin tekil ve çoğul isimlerini belirleyebiliriz (admin panelde gözükecek)
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        ordering=['id'] # bu şekilde admin panelinde id'e göre sıralanacak ',' vererek başka bir alan daha verebiliriz
    def __str__(self): # bu şekilde admin panelinde modelin title'ı gözükecek
        return self.title