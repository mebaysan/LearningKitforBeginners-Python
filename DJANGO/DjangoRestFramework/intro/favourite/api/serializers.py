from rest_framework.serializers import ModelSerializer, ValidationError
from favourite.models import Favourite


class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favourite.objects.filter(post=attrs['post'], user=attrs['user'])
        if queryset.exists():  # eğer bir kere favorilere eklenmiş bir psot varsa bir daha ekleyemesin
            raise ValidationError("Daha önce favorilere eklenmiş bir post tekrar eklenemez")
        return attrs


class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('content',)
