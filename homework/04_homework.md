1. 파이썬에서 변수를 찾을 때 접근하는 이름공간을 순서대로 작성하세요.

   Local scope : 정의된 함수

   Enclosed scope : 상위 함수

   Global scope : 함수 밖의 변수 혹은 import된 모듈

   Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성



2. 다음 중 틀린 것은? 답 : 1번
   (1) 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다. 

   (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다. 

   (3) 함수의 인자(parameter)는 함수 선언시 설정한 값이며, 인수(argument)는 함수 호출시 넘겨주는 값이다. 

   (4) 가변 인자를 설정할 때는 인자 앞에서 *을 붙이고, 이때는 함수 내에서 tuple로 처리된다.

답 :1번

2개를 리턴하는 것처럼 보이지만 실제로는 튜플 1개가 리턴되는 것으로 이는 하나의 튜플 객체 입니다. 



3. 재귀함수를 쓰는 장점과 단점을 작성하세요.

   장점 : 알고리즘을 코딩할 때에 직관적으로 표현할 수 있으므로, 이애하기가 쉽다.

   단점 : 계산되는 값이 많아지면, 그만큼 함수의 stack도 거미줄형태로 싸이게 되면서 계산시간이 늦어진다. 작성하기 어려움.