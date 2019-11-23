from import_export import resources
# import_export kütüphanesini kullanabilmek için gerekli
from app.models import Comment,Blog

class CommentResources(resources.ModelResource):
    class Meta:
        model = Comment #hangi model üzerinde import - export işlemi yapacağımızı belirtiyoruz

