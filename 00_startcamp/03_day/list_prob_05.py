'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')

# 아래에 코드를 작성해 주세요. split : 공백을 기준으로 하나하나 리스트로 만들어줌.
                            #split(';') : 괄호 안에 있는 것을 기준으로 리스트로 변환.
# print(prices)

# test = prices.split(';')

# print(test)


makes = prices.split(';')

boxes = []

for make in makes:
    boxes.append(int(make))

    #리스트에 요소를 추가하는 메서드. append()
    #list.append(1) 리스트에 1을 추가한다.

print(boxes)

boxes.sort(reverse=True)

for box in boxes:
    print(box)