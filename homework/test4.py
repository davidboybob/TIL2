# 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요. 

def bisection(x):
    if x < 0:
        return '양의 정수를 입력하세요.'

    half_value = 0
    for i in range(1000):
        # 입력된 x의 정수가 어떤 수 사이에 있는지 찾아내야 한다. 
        # 자연수 제곱의 값들 사이에 해당되면 그때의 자연수를 저장.
        if i**2 < x:
            small_one = i
            print(small_one)
        if i**2 > x:
            big_one = i
            print(big_one)
    # small 과 big의 사이값을 구해서 입력된 수 x와 비교.
        half_value = (small_one + big_one) / 2
        
        if half_value**2 < x:
            small_one = half_value
            print(small_one)
        if half_value**2 > x:
            big_one = half_value
            print(big_one)
    #방법 1 . half들의 리스트를 만들어서 숫자 찾아나가기
    #방법 2 . 직접 비교하면서 치환하기.
    


x = int(input())
# for i in range(100):
#         # 입력된 x의 정수가 어떤 수 사이에 있는지 찾아내야 한다. 
#         # 자연수 제곱의 값들 사이에 해당되면 그때의 자연수를 저장.
#     if i**2 < x:
#         small_one = i
        
#     if i**2 > x:
#         big_one = i
#         break
print(bisection(x))            
# print(big_one)
# print(small_one)