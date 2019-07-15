"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores1 = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

total_score = 0

for subject_score in scores1.values():
    # total_score = total_score + subject_score
    total_score += subject_score

# len(scores) len은 길이를 알려주는 함수
avg_score = total_score / 3
print(avg_score)

# 2. 반 평균을 구하시오. -> 전체 평균
scores2 = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

a_total_score = 0
b_total_score = 0

for a_subject_score in scores2.get('a').values():
    a_total_score += a_subject_score

a_avg_score = a_total_score / len(scores2.get('a'))

for b_subject_score in scores2.get('b').values():
    b_total_score += b_subject_score

b_avg_score = b_total_score / len(scores2.get('b'))
print(a_avg_score)
print(b_avg_score)

total_score2 = a_total_score + b_total_score
avg_score2 = total_score2 / (len(scores2.get('a'))+len(scores2.get('b')))
print(avg_score2)

# total_score = 0
# count = 0

# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score = total_score + indivisual_score
#         # total_score += indivisual_score
#         count = count + 1
#         # count += 1

# avg_score = total_score / count
# print(avg_score)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
seoul = 0

# for temperture in city.values():
#     for seoul in city.get('서울').key():
#         seoul_tem += seoul
#     for daejeon in city.get('대전').key():
#         daejeon_tem += daejeon
#     for Guagju in city.get('광주').key():
#         Guagju_tem += Guagju
#     for Busan in city.get('광주').key():
#         Busan_tem += Busan
    
# print(daejeon_tem)
# print(seoul_tem)

for name, temp in city.items():
    #1번째 돌때 name = 서울
    # temp = [-6, -10, 5]
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : {avg_temp:.2f}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# 첫번째로 for문이 돌때 기준점을 잡아야 합니다. : 여기서는 기준지역 : 서울, 기준온도 : 서울
# 두번째로 for문이 돌때 대전의 지역과 온도가 입력됩니다. 기존의 것(서울)과 비교합니다.
# 이때, 최고온도는 큰 값으로 대체하고, 최저 온도는 작은 값으로 대체합니다.

count = 0
for name, temp in city.items():
    #첫번째 시행 때 
    #name ='서울'
    #temp =[-6, -10, 5]
    #단 한번만 실행되는 조건이 필요. 변수 지정하여서 변수가 에 따라서 반복을 멈추거나 진행.

    if count == 0:
        hot_temp = max(temp)
        cold_temp = min(temp)
        hot_city = name
        cold_city = name
    else:
        #최저온도가 cold_temp 보다 낮으면, cold_temp 에 값을 새로 넣고,
        if min(temp) < cold_temp: #두번째 돌때이므로, temp는 대전의 값입니다.
            cold_temp = min(temp)
            cold_city = name
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
        #최고온다가 hot_temp 보다 높으면, hot_temp에 값을 새로 넣습니다.    
    count += 1

print(f'최고로 더웠던 지역은 {hot_city} : {hot_temp}, 최고로 추웠던 지역은 {cold_city} : {cold_temp}')



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')