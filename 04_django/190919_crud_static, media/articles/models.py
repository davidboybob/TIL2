from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

from django.urls import reverse
from django.db import models

# Create your models here.

def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'





class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # 나중에 추가하는 필드는 blank값 조건을 부여하여야 한다. 빈값설정
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source='image',
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality': 90},
    #     # upload_to='articles/images',
    # )


    image = ProcessedImageField(
        # ProcessedImageField 에 인자로 들어가 있는 값들은 migrations 이후에 
        # 추가되거나 수정되더라도 makemigrations 를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)], # 처리할 작업 목록
        format='JPEG', #저장 포맷
        options={'quality': 90}, #추가 옵션들
        upload_to=articles_image_path, #저장 위치 p
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        
        # return reverse('articles:detail', args=[self.pk]) #문자열로 출력
        return reverse('articles:detail', kwargs={'article_pk': self.pk}) #문자열로 출력
        # 주의 사항
        # reverse gkatndp args 랑 kwargs 를 동시에 인자로 보낼 수 없다.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'

'''
from django.urls import reverse
from django.db import models

class Question(modle.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=10)
    votes = models.IntegerField()

    def __str__(self):
        return self.content

'''

