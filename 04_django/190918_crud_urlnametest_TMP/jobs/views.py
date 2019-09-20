from django.shortcuts import render
import requests
from decouple import config
from faker import Faker
from .models import Job
from pprint import pprint

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')
    
    #db에 매칭되는 name 가져오기
    # Job.objects.get(name=name) => get 방식이 더 간단 하지만, 해당 데이터가 없을 경우 오류가 발생한다.
    #filter : 1개, 0개 상관없이 무조건 쿼리셋으로 가져옴.(리스트형식)
    person = Job.objects.filter(name=name).first()

    #db에 person이 있는지 없는지 판단
    if person: #기존 있는 값을 가져옴
        past_job = person.past_job 
    else: #db에 기존 이름이 없다면 (person 이 빈 쿼리셋(==False))
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job) # 새로운 레코드를 추가한다.
        person.save()

    # GIPHY (past_job)을 API 에 요청을 뵤내서 )
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1&rating=R'
    data = requests.get(url).json()
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    
    except IndexError:
        image = None

    context = {'person': person, 'image': image,}
    return render(request, 'jobs/past_life.html', context)