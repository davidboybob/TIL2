1. 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 구분 하시오.

  

  `String, List, Tuple, Range, Set, Dictionary`



mutable 변경가능한 것 : List, set, Dictionary(value만 key는 불변)

immutable 변경 불가능 한것 : String, Tuple, Range





2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

   ```python
   list(range(51)[1::2])
   ```
   
   ```python
   a = list(range(1,51))
   b = a[0::2]
   print(b)
   ```
   
   



3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.

   info = { 'student1': 'kim',
   	        	'student1': 'Lee',
       		    'student2': 'pak',

   ​			}

