from flask import Flask, render_template, request
import requests
from decouple import config


app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')




@app.route('/')
def hello():
    return 'Hi there!'

#view 함수 만들기
#1. 봇이 답장하는 페이지
#2. 답을 보내주는 페이지

@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    text = request.args.get('message') 
    

    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.html')


# web hook 작업
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
    # print(request.get_json())
    
    from_telegram = request.get_json()


    if from_telegram.get('message') is not None:        # 잘못보냈을 경우를 방지

        # step 2. 그대로 돌려보내기
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        

        #한글 키워드 받기
        #'/번역'으로 입력이 시작된다면, 파파고로 번여기 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            # .get이 아니라 .post로 써야한다. post 방식은 headers와 data를 같이 담아서 보낸다.
            # print(papago_res.json()) # text 변수 잡기 전에 프린트하여 확인해보자.
            text = papago_res.json().get('message').get('result').get('translatedText')

        if text[0:4] == '/로또 ':
            #회차번호를 받아온다.
            num = text[4:]
            #동행 복권에 요청을 보내 응답을 받는다.
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            # Json 형태로 바꿔준다. 크롬
            lotto = res.json()
           

            #1. 당첨번호 6개를 가져오기
            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num =lotto['bnusNo']
            text = f'로또{num}회차의 당첨 번호는 {winner} 입니다. 2등 보너스 번호는 {bonus_num}입니다.'




        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200

