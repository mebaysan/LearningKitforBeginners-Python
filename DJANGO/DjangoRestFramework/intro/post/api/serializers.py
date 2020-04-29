from post.models import Post
from rest_framework import serializers


# class PostSerializer(serializers.Serializer): # bu şekilde ilgili modele tekrar bir serializer model tanımlarız filed'a field
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField(max_length=255)


# fakat gözümüzün nuru ModelSerializer bizi bu zahmetten kurtarır
class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:api:detail',  # namespace alarak hangi view'a gidecek
        lookup_field='slug'  # hangi field'a göre
    )
    username = serializers.SerializerMethodField(method_name='username_getir') # Serializer method field denir, istediğimiz şekilde gösterebiliriz
    modified_by = serializers.SerializerMethodField(method_name='modified_getir')

    class Meta:
        model = Post  # hangi model ile çalışacağımızı set ediyoruz
        fields = [  # hangi field'lar ile çalışacağımızı belirtiyoruz
            # 'user',
            'username', # Serializer Method Fieldname
            'modified_by',
            'title',
            'content',
            'image',
            # 'slug',
            'url',
            'created_date',
            'modified_date',
        ]

    def username_getir(self, obj):
        return str(obj.user.username)

    def modified_getir(self, obj):
        if obj.modified_by:
            return str(obj.modified_by.username)
        return "Henüz Güncellenmemiş"
    # def save(self, **kwargs):
    #     return True

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title',instance.title) # gelen datanın tite'ı al yoksa instance.title al
    #     return instance

    # def create(self, validated_data):
    #     return Post.objects.create(user=self.context['request'].user,**validated_data) # instance'in user'i request.user dedik

    # def validate_title(self,value): # hangi field'ı kontrol edecek isek, validate_fieldadi
    #     if value == 'istenmeyen':
    #         raise serializers.ValidationError('Bu değer olmaz') # hata döndürdük
    #     return value

    # def validate(self, attrs):  # spesifik bir data'yı değil, bütün field'ları validate eder
    #     if attrs['title'] == 'istenmeyen':
    #         raise serializers.ValidationError('Bu değer olmaz')
    #     return attrs


"""

from post.models import Post
from post.api.serializers import PostSerializer

obj = Post.objects.first() # ilk Post objeyi seçtik

new = PostSerializer(obj) # seçtiğimiz objeyi serialize ettik
new.data # serialize edilmiş veriye ulaşıyoruz
>>> {'title': 'İlk Post', 'content': 'ilk post içeriği'}

veri = {'title':'Deneme Başlık'} # dict tipinde bir obje oluşturduk
yeni = PostSerializer(data=veri) # serializer objenin data arg'a veri'yi yolladık
if yeni.is_valid(): # eğer validate işlemlerini geçtiyse
     yeni.save() # serialize objeyi kaydet
else:
     print(yeni.errors) # değilse hataları ekrana bastır
 
>>> {'content': [ErrorDetail(string='This field is required.', code='required')]} # veri değişkeninde content vermedik

veri = {'title':'Deneme Başlık','content':'Deneme İçerik','user':1}
yeni = PostSerializer(data=veri)
yeni.is_valid()
>>> True
yeni.save()
>>> <Post: Deneme Başlık>


obj = Post.objects.first() # obje seçtik
data = {'title':'yeni title','content':'yeni içerik'} # data oluşturduk
islem = PostSerializer(obj, data=data) # güncellemek için mevcut objenin data'sını yeni data ile değiştiriyoruz
islem.is_valid() # eğer işlem valid ise
>>> True
islem.save() # işlemi execute et
>>> <Post: yeni title>




obj.delete() # yakaladığımız objeyi siler
>>> (1, {'post.Post': 1})

"""
