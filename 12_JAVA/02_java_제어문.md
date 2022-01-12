# 2. java 제어문

- if, while, for 등의 제어문에 대해서 알아보자.
- 집을 짓는 경우를 생각해 보자. 나무, 돌, 시멘트 등은 집을 짓기 위한 재료가 될 것이고, 철근 같은 것은 집의 뼈대가 될 것이다. 이것은 프로그램의 경우와 매우 비슷하다. 즉 나무, 돌, 시멘트 등의 재료는 바로 자료형이 될 것이고, 집의 뼈대를 이루는 철근이 바로 우리가 이 곳에서 알아볼 제어문이 될 것이다. 즉, 자료형을 그 근간으로 하여 그것들의 흐름을 원활회 효율적으로 만들어 주는 것, 이것이 바로 지금 부터 공부할 제어문이다.



## 2.1. 조건문

- if문의 기본 구조

  - if, else의 기본 구조

  ```java
  if (조건문) {
      <수행할 문장 1>
      <수행할 문장 2>
      ...
  } else {
      <수행할 문장 A>
      <수행할 문장 B>
      ...
  }
  ```

  

- 조건문이란 무엇인가?

  - `if (조건문)` 에서 사용되는 조건문이란 참과 거짓을 판단하는 문장을 말한다.

  ```java
  boolean money = true;
  if (money) {
      ...
  }
  ```

  조건문은 money가 되고 money 는 true 이기 때문에 if 문 다음의 문장을 수행하게 된다.

- 비교 연산자

  - 조건판단을 하는 경우는 자료형 (boolean) 보다는 비교 연산자(<, >, ==. !=. >=, <=) 를 쓰는 경우가 훨씬 많다.

    | 비교 연산자 | 설명                   |
    | ----------- | ---------------------- |
    | x < y       | x가 y 보다 작다        |
    | x > y       | x가 y 보다 크다        |
    | x == y      | x와 y 가 같다          |
    | x != y      | x와 y 가 같지 않다     |
    | x <= y      | x가 y 보다 크거나 같다 |
    | x >= y      | x가 y 보다 작거나 같다 |

  - x에 3을 y에 2를 대입한 다음에 x > y 라는 조건문을 출력하니 true가 출력된다. 그 이유는 x > y 라는 조건문이 참이기 때문이다.

  - `System.out.println(x < y);` : flase

  - `System.out.println(x == y);` : flase 

  - `System.out.println(x != y);` : true

  

  - "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라

  ```java
  int money = 2000;
  if (money >= 3000) {
      System.out.println("택시를 타고 가라");
  } else {
      System.out.println("걸어가라");
  }
  ```

  조건문이 거짓이 되므로, else 다음 문장이 수행된다.

- and(&&), or(||), not(!)

  - 또 다른 조건 판단에 쓰이는 것으로 and, or, not이란 것이 있다.
  - ` x || y` : x와 y 둘중에 하나만 참이면 참이다.
  - `x && y` : x와 y 모두 참이어야 참이다
  - `!x` : x가 거짓이면 참이다

  

  - "돈이 3000원 이상 있거나 풀러줄 시계가 있다면 택시를 타고 그렇지 않으면 걸어가라"

  ```java
  int money = 2000;
  boolean watch = true;
  
  if (money >= 3000 || watch) {
      System.out.println("택시를 타고 가라");
  } else {
      System.out.println("걸어가라");
  }
  ```

- contains

  - List 자료형에는 해당 아이템이 있는지 조사하는 contains라는 메소드가 있다. contain메소드는 조건문에 많이 활용 되는데 어떻게 활용이 되는 지 살펴보도록 하자.
  - "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라"

  ```java
  ArrayList pocket = new ArrayList();
  pocket.add("paper");
  pocket.add("handphone");
  pocket.add("money");
  
  if (pocket.contains("money")) {
      System.out.println("택시를 타고 가라");
  } else {
      System.out.println("걸어가라");
  }
  ```

  pocket 리스트 안에 'money' 가 잇으므로 `pocket.contains("money")` 는 참이 되어서 if문 다음의 문장이 수행되었다.

- else if (다중 조건 판단)

  - if와 else만을 가지고서는 다양한 조건 판단을 하기가 어렵다. 당므과 같은 예만 하더라도 if와 else만으로는 조건 판단에 어려움을 겪게 된다.
  - "지갑에 돈이 있으면 택시를 타고, 지갑엔 돈이 없지만 시계가 있으면 택시를 타고, 돈도 없고 시계도 없으면 걸어가라"

  ```java
  // 위의 문장을 보면 조건을 판단하는 부분이 두 군데가 있다. 먼저 지갑에 돈이 있는지를 판단해야 하고 지갑에 돈이 없으면 다시 시계가 있는지를 판단한다.
  
  
  // if 와 else 만으로 만든 코드
  boolean watch = true;
  ArrayList pocket = new ArrayList();
  pocket.add("paper");
  pocket.add("handphone");
  
  if (pocket.contains("money")) {
      System.out.println("택시를 타고 가라");
  } else {
      if (watch) {
          System.out.println("택시를 타고 가라")
      } else {
          System.out.println("걸어가라")
      }
  }
  
  
  // else if 사용한 코드
  boolean watch = true;
  ArrayList pocket = new ArrayList();
  pocket.add("paper")
  pocket.add("handphones");
  
  if (pocket.contains("money")) {
      System.out.println("택시를 타고 가라");
  } else if (watch) {
      System.out.println("택시를 타고 가라");
  } else {
      System.out.println("걸어가라");
  }
  ```

  - else if 개수에 제한 없이 사용할 수 있다.

- switch / case 문의 기본 구조

  - if 문과 비숫하지만 좀 더 정형화된 모습의 제어문이다.

  ```java
  switch (입력변수) {
      case 입력값1: ...
          break;
  ...
      default;...
          break;
  }
  ```

  - 입력변수의 값과 일치하는 case 입력값 ( 입력값1, 입력값2, ...) 이 있다면 해당 case 문 하위의 문장ㅇ ㅣ실행된다. case문마다 break 라는 문장이 있는데 해당 case문을 실행 항 뒤 switch 문을 빠져나가기 위한 것이다. 만약 break 문이 빠져 있다면 그 다음의 case문이 실행되게 된다.

  ```java
  public class SwitchDemo {
      public static void main (string[] args) {
          int month = 8;
          String monthString;
          switch (month) {
              case 1: monthString = "January";
                  break;
              case 2: monthString = "February";
                  break;
              case 3: monthString = "March";
                  break;
              case 4: monthString = "April";
                  break;
              case 5: monthString = "May";
                  break;
              case 6: monthString = "June";
                  break;
              case 7: monthString = "July";
                  break;
              case 8: monthString = "August";
                  break;
              case 9: monthString = "September";
                  break;
              case 10: monthString = "October";
                  break;
              case 11: monthString = "November";
                  break;
              case 12: monthString = "December";
                  break;
              default: monthString = "Invalid month";
                  break;
          }
          System.out.println(monthString);
      }
  }
  ```

  switch 문의 입력으로 1 이라는 숫자가 올 경우  "January" 라는 문자열이 12가 입력으로 올 경우 "December" 라는 문자열이 출력되는 예제이다. 위의 예는 month가 8로 고정되어 있기 때문에 "Agust" 라는 문자열이 출력될 것이다.

  - 위 switch 문은 month 의 값이 1 이면 case 1: 문장이 실행되고 2 이면 case 2: 문장이, 3이면 case 3: ... 이런 식으로수행되게 된다. 만약 month에 1에서 12사이의 숫자가 아닌 다른 값이 저장되어 있다면 default: 문장이 수행될 것이다.
  - 위와 같이 입력값이 정형화되어 있는 경우 if문보다는 switch/case문을 쓰는 것이 가독성에서 좀 더 유리하다.
  - switch/case 문은 if else 구조로 변경이 가능하지만 if else 구조로 작성된 모든 코드를 switch 문으로 변경할 수는 없다.



## 2.2. 반복문

- for 문은 예제를 통해서 알아보는 것이 쉽다.

```java
String[] numbers = {"one", "two", "three"};
for (int i = 0; i < 3; i ++) {
    System.out.println(numbers[i]);
}

// 결과

one
two
three
```

`numbers` 라는 배열의 첫번째 요소부터 마지막 요소까지 출력하는 예.

for의 조건문은 세미콜론(;)을 구분자로 세 부분으로 나뉘어진다.



for (초기치; 조건문 ; 증가치)

위의 예시 에서는 `초기치 : int i = 0`, `조건문 : i < 3`



- "총 5명의 학생이 시험을 보았는데, 시험점수가 60점이 넘으면 합격이고, 그렇지 않으면 불합격이다. 합격인지 불합격인지에 대한 결과를 보여준다."

```java
int[] marks = {90, 25, 67, 45, 80};

for (int i =0; i < 5 ; i++) {
    if (marks[i] >= 60) {
        System.out.println((i+1) + "번 학생은 합격입니다.")
    } else {
        System.out.println((i+1) + "번 학생은 불합격입니다.")
    }
}
```

i 값이 1씩 증가하며 for 문 안의 문장들이 수행된다. 따라서 marks[i]는 차례로 90, 25, 67, 45, 80 의 값을 갖게 된다. marks[i] 가 60 이상이면 합격 메시지를 출력하고, 60을 넘지 않으면 불합격 메시지를 출력한다.  i 가 marks의 갯수인 5보다 크게되면 for 문이 중지된다.



- for 과 continue

  - for문 안의 문장을 수행하는 도중에 continue 문을 만나면 for문의 처음으로 돌아가게 된다.

  ```java
  int[] marks = {90, 25, 67, 45, 80};
  
  for (int i = 0 ; i < 5; i++) {
      if (marks[i] < 60) {
          continue;
      }
      System.out.println((i+1) + "번 학생 축하합니다. 합격입니다.")
  }
  ```

  - 점수가 60점 미만인 학생일 경우에는 marks[i] < 60 이 참이 되어 continue 문이 수행된다. 따라서 축하 메시지를 출력하는 부분을 수행하지 않고 for문의 첫부분으로 돌아가게 된다.



- for each 문

  - for each 는 J2SE 5.0 부터 추가되엇다. for each 라는 키워드가 따로 있는 것은 아니고 동일한 for를 이용한다. 하지만 조건식 부분이 조금 다르다. 보통 다른 언어에서 for each라고 많이 하므로 자바에서도 보통 for each 문이라고 말한다.

  ```java
  String[] numbers = {"one", "two", "three"}
  for (String number; numbers) {
      System.out.println(number);
  }
  
  // for each 구조
  
  for (type var: iterate) {
      body-of-loop
  }
  ```

  - iterate는 루프를 돌릴 객체이고 iterate 객체에서 한개 씩 순차적으로 var에 대입되어 for문을 수행하게 된다. iterate 부분에 들어가는 타입은 루프를 돌릴 수 있는 형태인 배열 및 ArrayList 등이 가능하다.
  - 따로 반복회수를 임의로 주는 형태가 아니라면 for each 를 이용해서 훨씬 간단하게 작성할 수 있다. 루프를 핸들링 할 수는 없기 때문에 1 스탭씩 순차적으로 반복ㅎ라 때만 사용가능하다는 제약이 있다.





- While 문

  - 반복해서 문장을 수행해야 할 경우 while문을 사용한다.
  - 다음은 while 문의 기본 구조이다.

  ```java
  while (조건문) {
      < 수행할 문장 1>
      < 수행할 문장 2>
      < 수행할 문장 3>
  }
  ```

  - 조건문이 참인 동안 while문 아래의 문장들을 계속해서 수행 하게 된다.
  - "열번 찍어 안 넘어 가는 나무 없다." 라는 속담을 적용시켜 보면 다음과 같이 될 것이다.

  ```java
  int treeHit = 0;
  while (treeHit < 10) {
      treeHit++;
      System.out.println("나무를" + treeHit + "번 찍었습니다.");
      if (treeHit == 10) {
          System.out.println("나무 넘어 갑니다.");
      }
  }
  
      
  //결과는 다음과 같을 것이다.
   
  
  나무를 1번 찍었습니다.
  
  나무를 2번 찍었습니다.
  
  나무를 3번 찍었습니다.
  
  나무를 4번 찍었습니다.
  
  나무를 5번 찍었습니다.
  
  나무를 6번 찍었습니다.
  
  나무를 7번 찍었습니다.
  
  나무를 8번 찍었습니다.
  
  나무를 9번 찍었습니다.
  
  나무를 10번 찍었습니다.
  
  나무 넘어갑니다.
  ```

  - 위의 예에서 while 문의 조건문은 treeHit < 10 이다. 즉, treeHit가 10 보다 작은 동안에 while 문 안의 문장들을 계속 수행하게 된다. while문 안의 문장을 보면 제일 먼저 treeHit++ 로 treeHit 값이 계속 1씩 증가한다. 그리고 나무를 treeHit번 만큼 찍었음을 알리는 문장을 출력하고, treeHit가 10 이 되면 "나무 넘어갑니다."라는 문장을 출력하고 treeHit < 10 이라는 조건문이 거짓이 되어 while 문을 빠져 나가게 된다.
  - 여기서 treeHit++ 는 프로그래밍을 할 때 매우 자주 쓰이는 기법으로 treeHit 값을 1만큼씩 증가시킬 목적으로 쓰이는 것이다. == treeHit += 1처럼 쓰기도 한다.

- 무한루프(loop)

  - 무한 루프라 함은 무한히 반복한다는 의미이다. 자바에서 무한루프는 while문으로 구현 할 수가 있다. 

  ```java
  while (true) {
      <수행할 문장1>
      <수행할 문장2>
  }
  ```

  while의 조건문이 true 이므로 조건문은 항상 참이 된다. while은 조건문이 참인 동안에 while에 속해 있는 문장들을 계속해서 수행하므로 위의 예는 무한하게 while문 내의 문장들을 수행할 것이다.

  다음의 예를 보자

  ```java
  while (true) {
      System.out.println("Ctrl-C를 눌러야 while문을 빠져 나갈 수 있습니다.")
  }
  ```

  - 컨트롤 C 버튼으로 중지하자.



- while문 빠져 나가기(break)

 

while 문은 조건문이 참인 동안 계속해서 while문 안의 내용을 수행하게 된다. 하지만 강제로 while문을 빠져나가고 싶을 때가 생기게 된다.

 

커피 자판기를 생각해 보자. 커피가 자판기 안에 충분하게 있을 때는 항상 "돈을 받으면 커피를 줘라" 라는 조건문을 가진 while문이 수행된다. 자판기가 제 역할을 하려면 커피의 양을 따로이 검사를 해서 커피가 다 떨어지면 while문을 멈추게 하고 "판매중지"란 문구를 자판기에 보여야 할 것이다. 이렇게 while문을 강제로 멈추게 하는 것을 가능하게 해 주는 것이 바로 break이다.

 

다음의 예는 위의 가정을 자바로 표현해 본 것이다.

 

예) break의 사용

------

int coffee = 10;

int money = 300;

 

while (money > 0) {

   System.out.println("돈을 받았으니 커피를 줍니다.");

   coffee--;

   System.out.println("남은 커피의 양은 " + coffee + "입니다.");

   if (coffee == 0) {

​      System.out.println("커피가 다 떨어졌습니다. 판매를 중지합니다.");

​      break;

   }

}

------

 

money가 300으로 고정되어 있으니까 while (money > 0)에서 money는 0보다 크기 때문에 항상 참이다. 따라서 무한 루프를 돌게 된다. 그리고 while문의 내용을 한번 수행할 때 마다 coffee--에 의해서 coffee의 개수가 한 개씩 줄어들게 된다. 만약 coffee가 0이 되면 if (coffee == 0) 라는 문장이 참이 되므로 if문 다음의 문장들이 수행이 되고 break가 호출되어 while문을 빠져 나가게 된다.

 

- while문 조건문으로 돌아가기(continue)

 

while문 안의 문장을 수행할 때 어떤 조건을 검사해서 조건에 맞지 않는 경우 while문을 빠져나가는 것이 아니라 다시 while문의 맨 처음(조건문)으로 돌아가게 하고 싶을 경우가 생기게 된다. 만약 1부터 10까지의 수중에서 홀수만을 출력하는 것을 while문을 이용해서 작성한다고 생각해 보자. 어떤 방법이 좋을까?

 

예) continue의 사용

------

int a = 0;

while (a < 10) {

a++;

if (a % 2 == 0) {

   continue;

}

   System.out.println(a);

}

위의 예는 1부터 10까지의 수 중 홀수만을 출력하는 예이다. a가 10보다 작은 동안 a는 1만큼씩 계속 증가한다. if (a % 2 == 0) (2로 나누었을 때 나머지가 0인 경우)이 참이 되는 경우는 a가 짝수일 때이다. 즉, a가 짝수이면 continue 문장을 수행한다. 이 continue문은 while문의 맨 처음(조건문: a<10)으로 돌아가게 하는 명령어이다. 따라서 위의 예에서 a가 짝수이면 System.out.println(a)는 수행되지 않을 것이다.





# 3. 배열

## 3.1. 배열의 선언과 크기

- 1 부터 10까지의 숫자들 중 홀수들의 집합은 다음과 같이 int 배열로 표현 할 수 있다.

  - `int[] odds` = {1,3,5,7,9};
  - 배열은 자료형 타입 바로 옆에 `[]` 기호를 사용하여 표현한다. 위 예제와 같이 `int` 자료형의 배열은 `int[]` 로 표현되었다.
  - 요일의 집합은 다음과 같이 String 배열로 표현 할 수 있다.

  `String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};`

  - 즉, 배열 이란 자료형의 종류가 아닌 자료형의 집합을 의미한다.

  > 위에서 알아본 배열은 모두 1차원 배열이다. 2차원, 3차원 등의 다차원 배열도 가능하다. 사실 2차원 이상의 배열은 프로그래밍 시 잘 사용되지 않는다.

- 배열의 값은 어떻게 접근할 수 있을까?

  - 위에서 만든 요일의 배열중 "목"에 해당되는 값만 얻으려면 다음과 같이 인덱싱을 이용하면 된다.

  ```java
  String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
  System.out.println(weeks[3]);
  // weeks[3] 은 배열의 4번째 항목을 의미 ( 자바는 0부터 숫자를 카운트)
  ```

- 배열의 길이 

  - 프로글매 작성 시 배열이 만들어 졌다면 십중팔구는 for문으로 배열값을 돌리기 마련이다. 이런 경우 배열의 길이만큼 for 문을 돌리는 것이 중요한데 이 밸열의 길이는 다음과 같이 length를 이용하여 구한다.

  ```java
  String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
  for (int i=0; i<weeks.length; i++) {
      System.out.println(weeks[i]);
  }
  ```

  - weeks 배열을 순서대로 출력하는 프로그램이다. length를 어떻게 사용했는지 눈여겨 보도록 하자.



## 3.2. 객체들의 배열

- 해당 콘텐츠 오류로 ㅜㅜ 프로그래머스 자바 입분으로 다시