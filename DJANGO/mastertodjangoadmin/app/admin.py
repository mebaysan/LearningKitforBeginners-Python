from django.contrib import admin
from django.db.models import Count

from app.models import Blog, Comment, Category, Place
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin  # 3rd party kütüphaneyi dahil ettik
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, \
    ChoiceDropdownFilter  # dropdown için gerekli
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter  # range filter 3rd party kütüphane
from leaflet.admin import LeafletGeoAdmin  # leaflet ile 3rd party kütüphane
from import_export.admin import ImportExportModelAdmin  # import - export yapabilmek için gerekli 3rd party
from app.resources import CommentResources  # resources içinde yazdığımız import - export class'ı dahil ediyoruz


class CommentInline(
    admin.StackedInline):  # Comment modeli ilgili Blog model altında admin panelde göstereceğimiz için TabularInline yaptık
    # class CommentInline(admin.TabularInline):    # iki şekilde de kullanımı vardır hangisi hoşunuza giderse.
    model = Comment  # Hangi Modeli çalışacağımızı belirttik
    fields = ('text', 'is_active')  # hangi alanlar listelenecek
    extra = 1  # bu sayede mevcut foreignlerhariç kaç adet bu instance için form olsun onu belirtiyoruz
    classes = (
        'collapse',)  # bu model için collapse class'ı belirledik. Bu sayede foreign key ile bağlandığı modelde (80.satır) collapse şeklinde gözükecek


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

    def get_queryset(self, request):  # custom queryset yazıyoruz
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comments_count=Count('comments'))
        return queryset

    def no_of_comments(self, blog):  # blog instance'in kaç adet yorumu var onu gösteriyoruz
        return blog.comments_count

    def get_actions(self, request):  # bu method sayesinde istediğimiz default gelen action'ları silebiliriz
        actions = super().get_actions(request)
        try:
            del actions['delete_selected']
        except KeyError:
            pass
        return actions
    def has_delete_permission(self, request, obj=None): # instance içine girince sol atta 'delete' butonunu kaldırıyoruz
        return False
    no_of_comments.short_description = "Comment Counts"
    list_display = (
        'title', 'date_created', 'is_draft',
        'days_since_creation',
        'no_of_comments')  # ilgili modelin sayfasında nesneler listelenirken gösterilecek alanlar
    list_filter = ('is_draft', ('date_created', DateTimeRangeFilter))  # hangi alanlara göre filtreleme yapabilelim

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
            'fields': ('is_draft', 'categories'),
            'description': 'Options to configure blog creation',  # bu sayede bu blocklara açıklama yazabiliriz
            'classes': ('collapse',)  # bir nevi css class gibi düşünebiliriz.
        }),
    )
    summernote_fields = ('body',)  # bu field'ın summernote olmasını istiyoruz
    inlines = (CommentInline,)  # instance oluştururken inline şekilde hangi class gözükecek.
    filter_horizontal = ('categories',)  # bu şekilde yatay olarak kategorileri belirleyebiliriz
    # filter_vertical = ('categories',) # bu şekilde de dikey olarak kategorileri belirleyebiliriz
    actions = ('is_draft_to_false', 'is_draft_to_true')  # yazdığımız action methodlarını kayıt ediyoruz


class CommentAdmin(ImportExportModelAdmin):  # import export yapacağımız modelleri bu class'tan inherit ediyoruz
    list_display = ('blog', 'text', 'date_created', 'is_active')
    list_editable = ('is_active',)  # listelenirken aynı zamanda editlenebilsin mi?
    list_per_page = 25
    list_filter = (('blog', RelatedDropdownFilter),)  # dropdown 3rd party uygulama böyle gerektirdiği için
    resource_class = CommentResources  # resources.py içerisinde yazdığımız class'ı belirtiyoruz. işlem yapılacak class olarak
    list_select_related = ('blog',)
    raw_id_fields = ('blog',)  # bir comment eklerken ilişkili olduğu tablo içerisinde arama yapmamızı sağlar


admin.site.register(Blog, BlogAdmin)  # admin sayfamıza modelimizi kayıt ediyoruz
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Place, LeafletGeoAdmin)
