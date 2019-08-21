from django.contrib import admin
from .models import Article #명시적 상대경로 표현

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성한다. , 무조건 들어가야 한다!! 
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    list_display_links = ('content',)   
    list_editable = ('title',)
    list_per_page = 4 # 기본값 100

admin.site.register(Article, ArticleAdmin)
