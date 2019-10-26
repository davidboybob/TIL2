from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):

    visit_num = request.session.get('visit_num', 0)
    request.session['visit_num'] = visit_num + 1
    request.session.modified = True

    articles = Article.objects.all()
    context = {'articles': articles, 'visit_num': visit_num,}
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    context = {'article': article, 'comment_form': comment_form, 'comments': comments, 'person': person,}
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
        else:
            return redirect('articles:detail', article.pk)
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {'form': form, 'article': article, }
    return render(request, 'articles/create.html', context)
   


