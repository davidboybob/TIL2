#딕셔너리 만들기 - 1
lunch = {
    '중국집' : '02-123-4567'
}

#딕셔너리 만들기 - 2
dinner = dict(중국집='111', 일식집='112')

#딕셔너리에 내용 추가하기

lunch['분식집'] = '000-000-0000'
print(lunch)

#딕셔너리 내용 가져오기
idol = {
    'bts': {
        '지민' : 25,
        'RM' : 24

    }
}

#RM의 나이는?
idol['bts']['RM']

print(idol['exo'])
print(idol.get('exo'))

idol.get('bts').get('RM')