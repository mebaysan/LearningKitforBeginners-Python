from django import forms
from .models import Blog

banned_list = ["menesbaysan@gmail.com", "ysbaysan@gmail.com"]


class IletisimForm(forms.Form):  # formlarında form olması için forms.Form'dan inherit edilmesi gerek
    isim = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=75, label='İsim',
                           required=False)  # label -> formda gözükecek kısım, required -> Zorunlu mu değil mi
    soyisim = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=75, label='Soyisim',
                              required=False)  # widget -> bu field'ın özelliklerini belirliyoruz. class verebiliriz.
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=75, label='Email',
                             required=True)
    email2 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=75,
                              label='Email Doğrula', required=True)
    icerik = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=1000, label='İçerik')

    # Yukarıdaki gibi tek tek widgetları belirtmeden bütün widgetları tek fonksiyon ile belirleyebiliriz
    def __init__(self, *args, **kwargs):
        super(IletisimForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['icerik'].widget = forms.Textarea(attrs={'class': 'form-control'})

    def clean_isim(self):  # isim alanı için kontrol yazıyoruz
        isim = self.cleaned_data.get('isim')  # formdan gelen isim değerini çektik
        if isim == 'empty':
            raise forms.ValidationError('{} adında nickname kullanılamaz...'.format('empty'))
        return isim  # mutlaka bir şey return etmeli

    def clean_email(self):  # bu clean'ler ile sadece ilgili alana (email) erişebiliriz. Geri kalana erişemeyiz
        email = self.cleaned_data.get('email')
        if email in banned_list:
            raise forms.ValidationError(
                '{} banlı bir email adresi olduğundan bu adres ile kayıt yapılamaz'.format(email))
        return email

    def clean(self):  # bu bütün formda arama yapar gibi düşünebiliriz
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            self.add_error('email', 'Emailler eşleşmiyor...')  # bunu clean_email altına error olarak ekler
            self.add_error('email2', 'Emailler eşleşmiyor...')
            # raise forms.ValidationError('Emailler eşleşmiyor...')


class BlogForm(forms.ModelForm):  # model formu olması için ModelForm class'ından inherit ediyoruz
    class Meta:
        model = Blog  # bu formun kullanacağı model
        fields = ['title', 'content', 'image', 'yayin_taslak',
                  'kategoriler']  # kullandığı model içerisinde hangi alanlar bu forma gelsin

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['kategoriler'].widget.attrs.update({'class': 'form-control'})

    def clean_content(self):
        icerik = self.cleaned_data.get('content')
        if len(icerik) < 10:
            raise forms.ValidationError(
                "Lütfen en az 10 karakter giriniz. Şu anda {} karakter girdiniz..".format(len(icerik)))
        elif (len(icerik) > 1000):
            raise forms.ValidationError(
                "Lütfen en fazla 1000 karakter giriniz. Şu anda {} karakter girdiniz..".format(len(icerik)))
        return icerik
