import hashlib
from django import template

register = template.Library() # 기존 template 라이브러리에 아래의 함수를 추가한다.


@register.filter # 이 부분!
def makemd5(email): # 함수 앞에 인자 
    return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()

