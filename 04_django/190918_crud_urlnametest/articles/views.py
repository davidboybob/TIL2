from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
  # embed()
  # articles = Article.objects.all()[::-1]
  articles = Article.objects.order_by('-pk')
  context = {'articles': articles,}
  return render(request, 'articles/index.html', context)

# def new(request):
#   return render(request, 'articles/new.html')

def create(request):
  # embed()
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')

  #1.
  # article = Article()
  # article.title = title
  # article.content = content
  # article.save()

    #2.
    article = Article(title=title, content=content)
    article.save()

  #3.
  # Article.objects.create(title=title, content=content)
    # return redirect('articles:detail', article.pk)
    return redirect(article)
  # NEW
  else: #GET 으로 들어왔을때
    return render(request, 'articles/create.html')

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  article.get_absolute_url()
  context = {'article': article,}
  return render(request, 'articles/detail.html', context)


def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
  else:
    return redirect(article)


# def edit(request, pk):
#   article = Article.objects.get(pk=pk)
#   context = {'article': article,}
#   return render(request, 'articles/edit.html', context)

def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
  else:
    context = {'article': article,}
    return render(request, 'articles/update.html', context)

    