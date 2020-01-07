from django.shortcuts import render, redirect
from comments.models import Comment
from news.models import News
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@login_required(
    login_url='/login/')  # bu şekilde login olmasını sağlıyoruz, eğer auth değilse login sayfasına (login_url='...') redirect oluyor
def get_all_comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'back/comment_list.html', context=context)


@require_http_methods(['POST'])
def add_comment(request, npk):
    news = News.objects.get(pk=npk)
    ctxt = request.POST.get('msg')
    cname = request.POST.get('name')
    cmail = request.POST.get('email')
    new_comment = Comment(name=cname, email=cmail, txt=ctxt, news=news)
    new_comment.save()
    news.comment_set.add(new_comment)
    return redirect('news:news_detail', pk=npk)


def delete_comment(request, cpk):
    comment = Comment.objects.get(pk=cpk)
    comment.delete()
    return redirect('comments:comment_list')


@login_required(login_url='/login/')
def publish_comment(request, cpk):
    comment = Comment.objects.get(pk=cpk)
    comment.is_published = True
    comment.save()
    return redirect('comments:comment_list')


@login_required(login_url='/login/')
def draft_comment(request, cpk):
    comment = Comment.objects.get(pk=cpk)
    comment.is_published = False
    comment.save()
    return redirect('comments:comment_list')
