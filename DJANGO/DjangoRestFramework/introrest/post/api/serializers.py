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
