from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Article(models.Model):
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk': self.pk})
    
class Comment(models.Model):
    aritcle = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-pk',)