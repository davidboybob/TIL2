v 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요. 



v sqrt() 사용 금지



조금더 머리를 쓰자 - 이분법



1.25^2 = 1.5625 < 2 < 1.5^2 = 2.25



```python
#1. 루트2의 근사값 

import math
math.sqrt(2)

#2.
#양의 정수 n을 입력받아 제곱근의 근사값(제곱했을 때 n이 되는 수)를 반환하는 함수를 작성.
def my_sqrt(n): 
	x, y = 1, n # x가 왼쪽기준, y가 오른쪽기준.
    result = 1
    
    #제곱근의 제곱(result**2)과 입력 값(n)의 차이가 적어도 이 정도 차이보다 작아지면
    #같다고 본다. while문이 종료된다.
    while abs(result**2 - n) > 1e-10 # 1곱하기 10의 -10승
        result = (x+y)/2 # 양쪽 끝 값을 더해서 2로 나눔 : 절반값
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다.

        if result**2 < n: # 범위를 좁히면서 무엇을 바꿀 것인가? x인가 y인가
            x = result
        else:
            y = result
    return result

#3 is close
import math

def my_sqrt(n):
    x, y = 1, n
    result = 1
    
    while not math.isclose(result**2, n):
        result = (x+y)/2
        if result**2 < n:
            x = result
        else:
            y = result
    return result

```







