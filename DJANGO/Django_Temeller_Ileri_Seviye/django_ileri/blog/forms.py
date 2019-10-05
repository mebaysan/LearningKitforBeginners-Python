from django import forms


class IletisimForm(forms.Form):  # formlarında form olması için forms.Form'dan inherit edilmesi gerek
    isim = forms.CharField(max_length=75, label='İsim',
                           required=False)  # label -> formda gözükecek kısım, required -> Zorunlu mu değil mi
    soyisim = forms.CharField(max_length=75, label='Soyisim', required=False)
    email = forms.EmailField(max_length=75, label='Email', required=True)
    icerik = forms.CharField(max_length=1000, label='İçerik')
