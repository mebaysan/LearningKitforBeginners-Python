from rest_framework import serializers
from post.models import Post


# serializer'lar verileri JSON ve XML'e çevirmemize yarar

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=200)


class PostSerializer(
    serializers.ModelSerializer):  # bu şekilde bir modele uygun serializer yapabiliriz (model formlar gibi)
    class Meta:
        model = Post  # modeli belirtiyoruz
        fields = [  # hangi alanları istediğimizi belirtiyoruz
            'title',
            'content',
            'image',
            'slug',
            'created',
            'user',
            'modified_by',
        ]


"""
                Shell ile manuel ekleme ve Serializer Mantığı
from post.api.serializers import PostSerializer
veri = {"title":"shell'den eklenen","content":"shell'den eklenen güzel bir şeye benziyor. aynı zamanda rest framework'de güzelmiş :P"}
eklenen = PostSerializer(data=veri)
if eklenen.is_valid():
    eklenen.save()
else:
    print(eklenen.errors)



"""
###################################################

"""
                                Shell ile manuel güncelleme
            Güncelleme
from post.api.serializers import PostSerializer
from post.models import Post
obj = Post.objects.get(pk=1) # objeyi yakaladık
data = {'title':'değişen başlık','content':'değişen içerik'} 
islem = PostSerializer(obj,data=data)# yakaladığımız objeyi bu data ile değiştir diyoruz
islem.is_valid() # eğer true ise
islem.save() # islemi yapıyoruz



"""
