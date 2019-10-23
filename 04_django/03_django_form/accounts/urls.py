from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='password'),
    path('<username>/', views.profile, name='profile'), #문자열을 포함한 url 주소는 모든 조건을 내포하기 때문에, 최하단으로 내려줘야 합니다. 위에서 아래로 읽는 장고의 특성!
    
]
