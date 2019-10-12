from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify


class Kategori(models.Model):
    isim = models.CharField(max_length=30, verbose_name='Kategori Adı')

    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.isim


class Blog(models.Model):  # her model bir tabloya denk gelir. Buradaki 'Blog' aslında bizim tablomuzdur.
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık',
                             help_text='Başlık Bilgisi Burada Girilir')
    # CharField -> karakter alanı , max_length -> Max karakter uzunluğu zorunludur, verbose_name -> Formda nasıl gözükeceği, help_text -> Formun altında bilgi olarak gözükecek metin, blank -> formda boş girilip girilmemesi, null -> veritabanına boş kayıt edilip edilememesi
    content = models.TextField(max_length=1000, verbose_name='İçerik', null=True, blank=False)
    created_date = models.DateField(auto_now_add=True,
                                    auto_now=False)  # auto_now_add -> oluşturulma tarihini otomatik ekler, auto_now -> Bu nesne her değişime uğradığında otomatik olarak created_date'i güncellenir
    slug = models.SlugField(null=True, unique=True,
                            editable=False)  # editable=False -> admin panelden buraya müdahale edilemez
    kategoriler = models.ManyToManyField(to=Kategori, null=True,
                                         related_name='post')  # bir blog'un birden çok kategorisi olabilir
    image = models.ImageField(verbose_name="Resim", blank=True, null=True, help_text="Kapak Fotoğrafı Seçiniz",
                              default="default/default.png") # default -> eğer resim yoksa git media/default/default.png yi getir

    class Meta:  # bu class altına bu modelin tekil ve çoğul isimlerini belirleyebiliriz (admin panelde gözükecek)
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        ordering = [
            'id']  # bu şekilde admin panelinde id'e göre sıralanacak ',' vererek başka bir alan daha verebiliriz

    def __str__(self):  # bu şekilde admin panelinde modelin title'ı gözükecek
        return self.title

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Blog.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            post = Blog.objects.get(slug=self.slug)
            if post.title != self.title:
                self.slug = self.get_unique_slug()
        super(Blog, self).save(*args, **kwargs)
        # daha save fonksiyonu işini bitirmeden biz burda override yaptık. Bu sayede modelin slug alanını set ettik.
