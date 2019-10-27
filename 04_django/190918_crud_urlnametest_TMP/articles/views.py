from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article, Comment
# Create your views here.
def index(request):
  embed()
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

def detail(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  comments = article.comment_set.all()

  article.get_absolute_url()
  context = {'article': article, 'comments': comments,}
  return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
  else:
    return redirect(article)


# def edit(request, pk):
#   article = Article.objects.get(pk=pk)
#   context = {'article': article,}
#   return render(request, 'articles/edit.html', context)

def update(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method == 'POST':
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.article_pk)
  else:
    context = {'article': article,}
    return render(request, 'articles/update.html', context)



def comments_create(request, article_pk):
  #댓글을 달 게시글이 필요
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        #form 에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article)
        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)
    else:
        return redirect(article)


def comments_delete(request, article_pk, comment_pk):
  # article = Article.objects.get(pk=article_pk)
  comment = Comment.objects.get(pk=comment_pk)
  if request.method == 'POST':
    comment.delete()
  # return redirect(article)
  return redirect('articles:detail', article_pk)
  