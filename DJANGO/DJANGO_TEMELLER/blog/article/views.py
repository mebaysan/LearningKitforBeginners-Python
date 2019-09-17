from django.shortcuts import render, redirect, get_object_or_404, HttpResponse,reverse  # HttpResponse
from article.forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # login_required için
# Create your views here.
from article.models import Article,Comment


def index(request):  # bu değişken her view fonksiyonunda bulunmalı ve ilk parametre olmalı
    # return HttpResponse("RESPONSE DÖNDÜ")
    return render(request, "article/index.html")  # template'a veri gönderirken sözlük yapısı kullanmamız gerekli


# ilk parametre request olmak zorunda ve ikinci parametre templates altındaki hangi dosya olacağı

def about(request):
    return render(request, "article/about.html")


def detail(request, id):  # dinamik url oluşturduk, url'e id adında bir değişken gelecek
    # article = Article.objects.filter(id=id).first() # id'si requestten gelen id olan article'ı al
    article = get_object_or_404(Article,
                                id=id)  # hangi Modeli çekeceğimizi söylüyoruz ve neye göre çekeceğimizi söylüyoruz
    comments = article.comments.all() # model tarafında belirdeğimiz related_name sayesinde bu işlemi yapabildik
    return render(request, 'article/detail.html', {'article': article,'comments':comments})  # gelen article'yi yolladık


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    # article'lardan author kısmı mevcut login yapmış user olanları koy dedik
    return render(request, 'article/dashboard.html', {'articles': articles})


@login_required(login_url="user:login")
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(
            commit=False)  # bu form bir modelform olduğu için bunu kaydetmemiz çok kolay olacak. commit=False -> article objesini form fieldlardan oluştur fakat henüz save yapma
        article.author = request.user  # mevcut oturumdaki kullanıcı article'ın yazarı olsun
        article.save()  # bu sefer commiti yapıyoruz
        messages.success(request, "Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")

        messages.success(request, "Makale başarılı bir şekilde kayıt edildi")
        return
    return render(request, 'article/add_article.html', {'form': form})


@login_required(login_url="user:login")
def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None,
                       instance=article)  # instance ile formun datasına article'ı yoluyoruz
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi")
        return redirect("article:dashboard")
    return render(request, "article/update_article.html", {'form': form})


@login_required()
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "{} id'li Makale başarıyla silindi".format(id))
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword") # request içerisindeki name'i keyword olan değeri yakalıyoruz
    if keyword:
        articles = Article.objects.filter(title__contains=keyword) # articlelar içinde title fieldında keyword geçen articleları alıyoruz
        return render(request, "article/articles.html", {'articles': articles})
    articles = Article.objects.all()
    return render(request, "article/articles.html", {'articles': articles})


def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={'id':id})) # redirect yaparken parametreli url'lere bu şekilde yönlendirme yapılabilir