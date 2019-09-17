from django import forms


# django içerisindeki hazır form classı sayfaya dahil ettik

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    # label formun template kısmında nasıl görüntüleneceğidir aynı şekilde validatorleri girebiliriz
    password = forms.CharField(max_length=20, label="Şifre", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Şifre Doğrula", widget=forms.PasswordInput)

    def clean(self):  # django içerisindeki hazır method bunu override yapıyoruz
        username = self.cleaned_data.get("username")
        # username datasını alacak ve username değişkenine atayacak. burada validasyon işlemlerini yapabiliriz
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifre Eşleşmiyor")
            # hatayı raise ile yollayabiliriz. içine gidecek mesajı yazıyoruz
        values = {
            "username": username,
            "password": password
        }
        return values
        # işlem başarılı ise sayfaya return etmeliyiz. bunu sözlük yapısı ile return ediyoruz


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)