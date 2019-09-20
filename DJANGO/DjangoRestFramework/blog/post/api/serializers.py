from rest_framework import serializers
from post.models import Post

"""
            Serializer
aslında kısaca; modelleri json'a çevirmeye yarar
"""


# Normal serializer ile çalışırken alanları kendimiz elle belirmeliyiz.
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=200)


# Modelserializer ile çalışırken sadece modeli versek yeterlidir. ModelForm'lar gibi düşünebiliriz
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'slug', 'crated_date']
