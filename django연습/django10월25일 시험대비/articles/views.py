from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    visit_num = request.session.get('visit_num', 0)
    request.session['visit_num'] = visit_num + 1
    request.session.modified = True

    articles = Article.objects.all()

    context = {'aritcles': articles, 'visit_num': visit_num,}
    return render(request, 'articles:index', context)


