'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: ')) # input은 문자형이기 때문에 숫자로 바꾸기 위해 int를 사용

# 아래에 코드를 작성해 주세요.

for number in range(1, numbers+1):
    print(number)

for i in range(numbers):
    print(i+1)

    