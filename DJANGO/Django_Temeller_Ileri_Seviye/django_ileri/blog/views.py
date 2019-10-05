from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
from .forms import IletisimForm, BlogForm


def iletisim(request):
    form = IletisimForm(
        data=request.GET or None)  # formumuzdan bir instance oluşturuyoruz, data= -> eğer varsa GET'ten gelenleri al inputlara yerleştir yoksa boş geç
    # print(request.GET.get('email')) # GET içerisindeki değerleri yakalarız
    if form.is_valid():  # eğer formdan gelen bilgiler doğru ise
        isim = form.cleaned_data.get('isim')  # form içindeki bilgileri yakalayabiliyoruz
        soyisim = form.cleaned_data.get('soyisim')
        email = form.cleaned_data.get('email')
        icerik = form.cleaned_data.get('icerik')
        print(icerik, email, isim, soyisim)
    return render(request, 'blog/iletisim.html', {'form': form})  # formu contexte gönderiyoruz


def posts_list(request):
    posts = Blog.objects.all()
    if (request.GET.get('deneme')):
        get = request.GET.get('deneme')
        return render(request,
                      "blog/posts_list.html", context={
                'posts': posts, 'get': get})
    return render(request,
                  "blog/posts_list.html", context={
            'posts': posts})  # ilk önce zorunlu olarak request'i göndermeliyiz, daha sonra template'i daha sonra contexti. context bir sözlüktür


def post_update(request):
    return HttpResponse("update")


def post_delete(request):
    return HttpResponse("delete")


def post_create(request):
    form = BlogForm()
    if request.method == "POST":  # eğer method POST ise
        form = BlogForm(data=request.POST)  # yeni bir form oluştur ve oluşturduğun formun içine bu datayı yaz
        if form.is_valid():
            created_blog = form.save(
                commit=False)  # commit False olunca oluşacak nesneyi döndürür fakat veritabanına henüz ekleme yapmaz
            created_blog.save()  # commit False yaptığımız için oluşturduğumuz instance'i tekrardan kayıt ediyoruz
            return redirect('blog:posts_list')
    return render(request, 'blog/post_create.html', context={'form': form})
