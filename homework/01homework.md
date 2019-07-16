1. python 에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```pyhon
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

import keyword
print(keyword.kwlist)

```

2. 파이썬에서  float 는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.

   (floating point rounding error)

   따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

```python
a = 0.1 * 3
b= 0.3
```

---

```python
#method 1
import math
a= 0.1 * 3
b= 0.3
math.isclose(a, b)

#method 2
import sys
abs(a - b)<= sys.float_info.epsilon

#method 3
abs(a-b)<= 1e-10

```



3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요.

```python
print('줄바꿈 : \n')
print('탭 : \t')
print('\ : \\')
```



4. “ 안녕, 철수야 ” 를 String Interpolation을 사용하여 출력하세요.

```python
part_1= '안녕'
part_2= '철수야'

print('"{}, {}"'.format(part_1, part_2))

#f-string

f'"{part_1}, {part_2}"'

```



5. 다음 중 형변환시 오류가 발생하는 것은? 답 : 5

   1) str(1)      2) int(‘30’)  	3) int(5)       4) bool(‘50’)	 5) int(‘3.5’)



* float로 바꾸어야 한다.