import requests
from flask import Flask, render_template, request

#두개의 페이지와 두개의 함수
#1. 로또 회차/ 내 번호 입력 페이지 , 결과페이지
#2. 2개의 함수

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('lotto_result')
def lotto_result():
    #회차 번호를 받아온다.
    num = request.args.get('num')
    #동행 복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    lotto = res.json()
    # Json 형태로 바꿔준다. 크롬

    #1. 당첨번호 6개를 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    # 내 번호 리스트 만들기
    for num in request.args.get('numbers').split():
        numbers.append(int(num)) #num은 리스트의 값으로 str형태이다.

    #등수 가리기(몇개 맞았는지 교집합이 필요)
    matched = 0
    for num in numbers:
        if num in winner:
            matched += 1

    if matched == 6:
        result = '1등입니다!'

    elif matched == 5:
        if lotto['bnusNo'] in numbers:
            result = '2등입니다!'
        else:
             result = '3등입니다!'

    elif matched == 4:
        result = '4등입니다!'       
    elif matched == 3:
        result = '5등입니다!'       
    else:
        result = '꽝입니다.'


        return render_template('lotto_result.html', 
                                winner = winner, 
                                numbers = numbers, 
                                result = result)
