from django.contrib import admin
from app.models import Blog
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin  # 3rd party kütüphaneyi dahil ettik

"""
Bu projede kullanılan kütüphaneler requirements.txt içerisinde. Ne işe yaradıkları özetle burada;
*******************************
        Faker (pip install Faker)
from app.models import Blog # app.models içerisinden Blog modeli çağırdık
from faker import Faker # Faker modulü dahil ettik
faker = Faker() # faker instance oluşturduk
for _ in range(0,500):
    Blog.objects.create(title=faker.sentence(),body=faker.paragraph()) # 500 adet Blog instance oluşturduk faker sayesinde
*******************************
        Django TinyMCE / Django CKEditor / Django Summernote -> kullanabileceğimiz rich text editörler
pip install django-summernote -> bu uygulamada summernote kullanıldı.(https://github.com/summernote/django-summernote)

"""


class BlogAdmin(
    SummernoteModelAdmin):  # admin panelde modeli daha rahat yönetebilmek için bir AdminModel class'ı oluşturuyoruz
    def is_draft_to_false(self, request,
                          queryset):  # bu model için bir action yazıyoruz. request istek parametremiz. queryset ise seçtiğimiz class instance'leridir.
        count = queryset.update(is_draft=False)
        self.message_user(request, "{} blogs have been changed draft to False".format(
            count))  # bu sayede işlem gerçekleşince gözükecek mesajı da belirleyebiliriz.

    is_draft_to_false.short_description = "Change Draft to False"  # yazdığımız action fonksiyonuna özel bir isim belirlemek istersek short_description diyerek belirleyebiliriz

    def is_draft_to_true(self, request, queryset):
        count = queryset.update(is_draft=True)
        self.message_user(request, "{} blogs have been changed draft to True".format(count))

    is_draft_to_true.short_description = "Change Draft to True"

    def days_since_creation(
            self,
            blog):  # bu şekilde kendimize birer özellik yazabilir ve bunları admin panelde kullanabiliriz. bir blog instance alacağını belirttik
        diff = timezone.now() - blog.date_created
        return diff.days

    days_since_creation.short_description = "Days Active"  # bu şekilde yazdığımız özelliğe panelde gözükmesini istediğimiz ismi verebiliriz
    list_display = (
        'title', 'date_created', 'is_draft',
        'days_since_creation')  # ilgili modelin sayfasında nesneler listelenirken gösterilecek alanlar
    list_filter = ('is_draft', 'date_created')  # hangi alanlara göre filtreleme yapabilelim

    # ordering = ('title','-date_created') # hangi model fieldlarına göre sıralayacak. '-' verdiklerimiz büyükten küçüğe demektir
    def get_ordering(self, request):  # bu şekilde de custom ordering yazabiliriz
        if request.user.is_superuser:
            return ('title', '-date_created')
        return ('title',)

    search_fields = ('title',)  # hangi model field'a göre arama yapacağını belirleriz
    prepopulated_fields = {'slug': ('title',)}  # bu sayede title'ı yazarken; slug kendi kendine yazılacak
    list_per_page = 25  # sayfa başına kaç instance listelenecek onu belirliyoruz
    date_hierarchy = 'date_created'  # bu sayede tarihe göre sıralama butonu ekleyebiliriz sol üst, search bar altına
    # fields = (('title', 'slug'), 'body',
    #         'is_draft')  # bu sayede model field'larını yönetebiliriz. Hangisi gözükecek vs.. tuple içinde yazılanlar gruplanır aynı block'da gösterilir
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'body'),
        }),
        ('Advanced Options', {  # bu sayede field'ları gruplayabilir onların blocklarına isim verebiliriz
            'fields': ('is_draft',),
            'description': 'Options to configure blog creation'  # bu sayede bu blocklara açıklama yazabiliriz
        }),
    )
    summernote_fields = ('body',)  # bu field'ın summernote olmasını istiyoruz
    actions = ('is_draft_to_false', 'is_draft_to_true')  # yazdığımız action methodlarını kayıt ediyoruz


admin.site.register(Blog, BlogAdmin)  # admin sayfamıza modelimizi kayıt ediyoruz
