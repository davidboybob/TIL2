from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=20, required=True)
    content = forms.CharField(required=True)

    class Meta:
        model = Article
        # fields = {'title', 'content',}
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)