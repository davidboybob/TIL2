from django.db import models

# Create your models here.
class Article(models.Model): # models.Model의 상속을 받는다.
    #id(primary key)는 기본저긍로 처음 테이블 생성시 자동으로 만들어 집니다.
    # id = models.AutoField(primary_key=True) #AutoField 아이디값을 자동으로 입력되게 하는 인스턴스
    title = models.CharField(max_length=10) # 글자수 10글자로 제한 #클래스 변수 (DB의 컬럼)
    content = models.TextField() #무한정 들어갈 수 있는 텍스트 값
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ----------------------------- table을 만들기 위해서 설계한 것. model과 DB는 다른 것!
    # 클래스 변수는 소문자로만 작성!


    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'