from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from comment.models import Comment
from rest_framework import serializers
from post.models import Post

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_date', 'user']  # exclude (hariç) created_date bütün field'ları kullanacağım

    def validate(self, attrs):
        if attrs['parent']:  # parent'i varsa
            if attrs['parent'].post != attrs['post']:  # parent'in konusu ile kendisinin (self) konusu bir mi
                raise serializers.ValidationError('Yanlış giden bir şeyler var')

        return attrs


# class CommentChildSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug','id']


class CommentListSerializer(ModelSerializer):
    replies = serializers.SerializerMethodField(method_name='replies_getir')
    user = UserSerializer()
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = '__all__'  # bütün field'ları kullanacağım
        # depth = 1 # foreign key ile bağlı olan verilerin tüm bilgilerini getirir

    def replies_getir(self, obj):
        if obj.any_children:  # property'mizi kullandık
            return CommentListSerializer(obj.get_children(),
                                         many=True).data  # many=True -> birden fazla veri var, obj.get_children() -> Kendisine ait child yorumları gönderecek,  .data -> serialize edilmiş veri
            # return CommentChildSerializer(obj.get_children(),
            #                               many=True).data  # many=True -> birden fazla veri var, obj.get_children() -> Kendisine ait child yorumları gönderecek,  .data -> serialize edilmiş veri


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
