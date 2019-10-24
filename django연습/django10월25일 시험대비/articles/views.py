from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    visit_num = request.session.get('visit_num', 0)
    request.session['visit_num'] = visit_num + 1
    request.session.modified = True

    articles = Article.objects.all()

    context = {'articles': articles, 'visit_num': visit_num,}
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.commets_set.all()
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    comment_form = CommentForm()
    context = {'article': article, 'comments': comments, 'person': person, 'comment_form': comment_form,}
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

