from django.forms import ModelForm
from article.models import Article


# django bizim için otomatik olarak modelimize göre bir form oluşturacak
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'image',
        ] # Modeldeki hangi alanlara göre input oluştursun
