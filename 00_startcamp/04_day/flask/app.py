from flask import Flask, render_template, request
from datetime import datetime
import random



app = Flask(__name__)

#render template
@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html') 
    #app.py와 똑같은 위체에 template라는 폴더를 만들어야 합니다. 그안에 template를 넣어야 불러올 수 있습니다.


@app.route('/dday')
def dday():
    #오늘 날짜
    startgame = datetime.now()
    #수료 날짜
    endgame = datetime(2019, 11, 29)
    #수료날짜 - 오늘 날짜
    dday = endgame - startgame
    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄을 보내 봅시다</h1>
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
    </ul>

    """
# variable routing

# @app.route('/greeting/<string:name>')
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'반갑습니다!{name}'
    return render_template('greeting.html', html_name = name)


@app.route('/cube/<int:number>')
def cube(number):
    tripple = pow(number, 3)

    return render_template('cube.html', html_tripple = tripple, html_number = number)
    # return f'{number} 세제곱은 {number ** 3}입니다!'

#/lunch/몇명이 식사하는지 인원
#플라스크는 여러 메뉴 중에서 인원수 만큼의 메뉴를 응답합니다.

@app.route('/lunch/<int:person>')
def lunch(person):
    menu = ['레드코코넛누들', '하이라이스', '함박스테이크', '짬뽕']
    select = random.sample(menu, person)
    return str(select)

#render template




@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '알라딘', '라이온킹','엔드게임']
    return render_template('movie.html', movies=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    name = request.args.get('data') 
    return render_template('pong.html', name = name)


# https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
    return render_template('naver.html')
 


# https://www.google.com/search?q=김다미
@app.route('/google')
def google():
    return render_template('google.html')


#vonvon 만들기 , view 함수 2개, templates 2개(이름 받는 곳/ 결과 출력하는 곳)
@app.route('/inputvonvon')
def inputvonvon():
    return render_template('inputvonvon.html')


@app.route('/outputvonvon.html')
def outputvonvon():
    
    output = request.args.get('out')

    ability = ['지능', '매력', '못생김', '잘생김', '개밥쉰내','인싸력','돈']
    out1 = random.sample(ability, 3)  
    
    return render_template('outputvonvon.html', output = output, out1 = out1)