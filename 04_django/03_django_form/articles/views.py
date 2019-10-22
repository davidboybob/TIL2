from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

import hashlib

# Create your views here.
def index(request):
    #-------------------- hashlib // gravatar-----------------------
    # if request.user.is_authenticated:
    #     gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    # else:
    #     gravatar_url = None


    # embed()
    #------------ 인증 ------------------
    # session 에 visits_num 키로 접근해 값을 가져온다.
    # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면(방문한 적이 없다면) 0 값을 가져오도록 한다.
    visits_num = request.session.get('visits_num', 0)
    # 그리고 가져온 값을 session에 visits_num 에 매번 1씩 증가한 값으로 할당한다. (유저의 다음 방문을 위해 )
    request.session['visits_num'] = visits_num + 1
    # session 데이터 안에 있는 새로운 정보를 수정했다면, django는 수정한 사실을 알아채지 못하기 떄문에 다음과 같이 설정.
    request.session.modified = True # 세션에 대한 공식문서 참고 => 반복해야 하므로 setting 에서 설정
    # embed()
    #----------------------------------
    articles = Article.objects.all()
    #articles = get_list_or_404(Article)


    context = {'articles': articles, 'visits_num': visits_num,} # 'gravatar_url': gravatar_url 중복 없애기 부분

    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content,)
        # article.save()

        # form 인트턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding work)
        # 이 처리 과정은 binding 이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        #embed()
        # form 이 유효한지 체크한다.        
        if form.is_valid():
            # form.cleanc_data 로 정제된 데이터를 받는다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content,)
            article = form.save(commit=False)
            article.user = request.user
            article.save()
        return redirect(article)
            
    else:
        form = ArticleForm()
    # 상황에 따라 context 에 넘어가는 2가지 form
    # 1. GET : 기본 form
    # 2. POST : 검증에 실패 후의 form(is_valid == False)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)
    


def detail(request, article_pk):
    # try:
        # article = Article.objects.get(pk=article_pk)
    # except Article.DoesNotExist:
    #     raise Http404('No Article mathes the given query.')
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm() # 댓글 폼
    
    comments = article.comment_set.all() # Article의 모든 댓글
    context = {'article': article, 'comment_form': comment_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


@require_POST    
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
        else:
            return redirect(article) #detail
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                article.save()
                return redirect(article)
        else:
            # ArticleForm 을 초기화 ( 이전에 DB에 저장된 데이터를 넣어준 상태)
            # form = ArticleForm(initial={'title': article.title, 'content': article.content,})
            # # __dict__: article 객체 데이터를 딕셔너리 자료형으로 변환
            form = ArticleForm(instance=article)
    
        # 1. POST : 검증에 실패한 form (오류 메세지도 포함된 상태)    
        # 2. GET : 초기화된 form
    else:
        return redirect('articles:index')
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #객체를 Create 하지만, db에 케로드는 작성하지 않는다.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
    
    return redirect('articles:detail', article_pk)


@require_POST       
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)


def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    #django 최적화 o
    if article.like_users.filter(pk=request.user.pk).exists(): #get은 빈값일 때 오류가 뜨기 떄문에 사용 x
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')

    #in 을 이용한 방법 최적화 x
    # #해당 게시글에 좋아요를 누른 살마들 중에서 현재 접속유저가 있다면 좋아요를 취소
    # if request.user in article.like_users.all():
    #     article.like_users.remove(request.user) # 좋아요 취소 
    # else:
    #     article.like_users.add(request.user) # 좋아요 
    # return redirect('articles:index')
