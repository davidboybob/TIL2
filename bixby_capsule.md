[TOC]

# :egg: 빅스비 sw expert Academy

## :baby_chick:  1. 빅스비 소개

### :hatching_chick: 1.1 빅스비를 투자하는 이유 : 시대의 흐름, 패러다임의 변화



2017년 5월 처음으로 출시 => 이후에 많은 변화를 겪음, 

2018년 9월에는 확장성을 위해 아키텍쳐를 전면 수정 후 새로운 빅스비를 선보임.

여러기기에서 동작될 수 있는 확장성을 화복함.

에어컨, 등등 3개국어 => 8개국어로 확장 더 많은 언어 지원



---

### :hatching_chick: 1.2 Bixby developer studio 살펴보기

Capsule : bixby 서비스를 제공하기 위해서 bixby 플랫폼 서버에서 실행되는 최소단위의 bixby 서버 어플리케이션이다.

bixby 서비스 개발 = bixby 캡슐 개발



capsule_id 생성, 

example => 

playground => 서버에서 TEST x 외부로 노출 x



네임등록 => 빅스비 플랫폼에 실제적으로 사용자에게 서비스를 제공



플레이 그라운드 버거 #



문의 및 지원 : support@bixbydevelopers.com

웹 문의 : support.bixbydevelopers.com



---

## :baby_chick: ​2. Bixby Capsule개발 기본개념

### :hatching_chick: 2.1 Bixby 서비스 아키텍처와 Capsule 구조

#### 	2.1.1 Bixby 서비스 아키텍처 (Client - Server 아키텍처)

​	[음성인식과 자연어 이해]

ASR : 발화를 문자로 변화하는 기술

- 발화(Automatic Speech Recognition) : 사람이 말하는 음성언어 
- ex) Text : "오늘 서울 날씨 알려줘"

NLU (Natural Language Understanding) : 문장의 의미를 이해하는 기술

- ex) "오늘" : 날짜에 대한 정보 , "서울" : 지역에 대한 정보



##### **빅스비 서비스 아키텍쳐**

![제목 없음](https://user-images.githubusercontent.com/52685322/65370928-35122780-dc99-11e9-9637-402f4d6675df.png)

plan : 

- 일한 결과 값을 얻기 위해 필요한 할 일에 대한 순서도
- 캡슐을 기반으로 생성. 
- 빅스비 캡슐 코드를 바탕으로 동작을 실행하기 위하 계획을 가장 효율적인 방법으로 재구성한 것이 플랜그래피이다.



캡슐을 잘 만들어야만 캡슐이 잘 분류되고 발화의 의도를 정확히 파악되며 이 의도를 충족시키기 위해 코드가  적합하게 실행될 수 있습니다.



---

#### 	2.1.2 Capsule 구조 (모델링, 비즈니스 로직, UI/UX, 트레이닝)

##### **빅스비 Capsule 구조**

1. 모델링 : 발화 인식 및 발화 결과를 리턴할 때 필요한 값
   - Actions : 캡슐이 사용자가 원하는 작업ㅇ르 이해하도록 수행할 동작을 정의
2. 비즈니스 로직 
   - Javascript Code: 사용자가 원하는 작업을 실제 수행하는 코드, **이 단계에서 서비스 API 연동**
3. UI / UX 
   - Bixby Views : 최종결과를 사용자에게 보여주는 레이아웃 작업
   - Dialog : 사용자에게 되묻거나 결과를 응답해 주는 응답문을 생성
4. 트레이닝 
   - 발화 Training : Capsule이 잘 동작하도록, 처리할 수 있는 발화를 생성하고 자연어 트레이닝(NL Training )을 진행
   - Debugging : 개발한 캡슐이 구현한대로 동작하는지 확인

****



### :hatching_chick: 2.2 Bixby Capsule 개발기본개념 

#### 	2.2.1 Modeling

-  첫 개발 시 모델링 부분의 첫인상에서 다른 버츄어 어시스턴스 플랫폼과 차이를 크게 느끼는 부분.

- 모델링을 통해 체계적인 구조의 설계를 바탕으로 개발하는 것이 결과적으로는 나중에 훨씬 효율적이다.

- 다이나믹 프로그램 제너레이션을 통한 자동프로그래밍 => 일을 줄여주고, 더 다양한 캡슐을 수행할 수 있도록 해줌.

- 익숙하신 기존의 프로그래밍 언어의 문법을 채용  : JSON과 비슷함. (구조를 잘 파악하자! 어렵지 않다!)

  

##### **컨셉과 액션이란?**

- 빅스비 캡슐을 만드는 것은 사용자가 원하는 것을 이해해서 이를 실행해 줄 수 있도록 하는것.
- 사용자는 언어를 통해서 원하는 것을 기술 하고 빅스비는 여러분이 정의한 틀 모델에 따라서 이를 이해함
- 이를 바탕으로 사용자가 원하는 일을 수행



ex) 5 + 7은 무엇이지?

빅스비 플랫폼은 명령을 이해하기 위해서 문장을 적합한 단위 요소로 이해

`input1: 5`, `input2: +`, `input3: 7` 

`output : 12`

`concept : 적합한 단위요소`, `Action : 수행명령`

input concept를 가지고 output을 도출하는 것을 Action이라고 한다.

![캡슐의 컨셉 및 액션](https://user-images.githubusercontent.com/52685322/65371199-33962e80-dc9c-11e9-96ea-4e805c72c378.jpg)



##### **Modeling** 이란 ? 

![모델링이란](https://user-images.githubusercontent.com/52685322/65371216-693b1780-dc9c-11e9-8675-c3b4ea443a90.png)

​	Concept의 종류

​		primitives : boolean, integer, Decimal, Name, Text, Enum

​		Structures : property로 다른 Concept, Primitive구성



복잡한 코드가 아니므로, 잘 설계하는 것이 중요!

![예시](https://user-images.githubusercontent.com/52685322/65371252-e1094200-dc9c-11e9-902d-05e1f273fd47.jpg)

Concept Action Network(CAN)



---

#### 	2.2.2 Business Logic

- 주로 Javascript를 통해서 별도로 만듬.

- `javascript 명령문 파일`은 `endpoints.bxb`과 연동.

  ```javascript
  endpoits {
      action-endpoits {
          action-endpoint (ArithmeticOperation) {
              accepted-inputs (leftOperand, rightOperand, operator)
              local-endpoint (arithemticOperation.js)
          }
      }
  }
  ```

  



---

#### 	2.2.3 Training

- 자연어 트레이닝 부분
- 자세한 내용은 나중에 설명.

---

#### 	2.2.4 Views

- `.view`파일

![View 구조](https://user-images.githubusercontent.com/52685322/65371495-013a0080-dc9f-11e9-989b-41980b26e581.jpg)



---

### :hatching_chick: ​2.3 시뮬레이터와 디버깅 및 On-Device 테스트

#### 	2.3.1 시뮬레이터(Bixby Developer Studio에서의 발화 테스트 방법)



#### 	2.3.2 디버깅(Graphicla Trace와 Javascript Log를 활용한 디버깅 방법)

#### 	2.3.3 On-Device 테스트 (실제 디바이스 환경에서의 발화 테스트 방법)

## :baby_chick: ​3. Modeling 구현

### :hatching_chick: ​3.1 Modeling - Action & Concept

#### 	3.1.1 Action

- Action 뜯어보기

  ```python
  action (FindMovie) { #FindMoive => Action이름
    type (Search) #Type : Action의 종류를 설정하는 부분, Bixby 시스템이 Action을 검색할 때 힌트를 줌
    description (Find a movie by optional director, genre, rating, actor(s), and/or title.)
    collect {
      input (movieActor) {
        type (ActorName)
        min (Optional)
        max (Many)
      }
      input (movieDirector) { # Input : Action 실행에 필요한 입력 값ㅇ르 지정한느 부분
        type (DirectorName) #변수명 : Action에서 해당 Concept에 사용되는 이름
        min (Optional) #Min & Max : 발화로부터 이 input이 몇 개 받아들일지 결정 
          # Min -> Required : 꼭필요,
          #	  -> optional : 꼭 필요 x
          # Max -> one : 한 개
          # 	  -> Many : 여러 개
      }
      input (movieGenre) {
        type (MovieGenre)
        min (Optional)
      }
      input (movieRating) {
        type (MovieRating)
        min (Optional)
      }
      input (title) {
        type (MovieTitle)
        min (Optional)
      }
    }
    output (Movie) { # Action 실행의 결과
    }
  }
  ```

  

#### 	3.1.2 Concept

- Pirmitives : 기본 자료형
  - primitive 타입은 기본형 변수라고도 하며, 9가지가 있음
  - Bollean은 True/False를 저장하는 타입
  - Decimal은 실수형 숫자를 저장하는 타입
  - Integer은 정수형 숫자를 저장하는 타입
  - Enum은 열거할 수 있는 문자열을 저장하는 타입
  - Name은 짧은 문자열을 저장하는 타입
  - Qualified는 Name과 기본적으로 비슷하지만, 지정 패턴에 맞는 데이터를 저장
  - Text는 긴 문자열을 저장하는 타입
  - Text, Name, Enum 타입은 문자열을 저장하는 공통점이 있지만, NL 트레이닝시에는 역할이 상이.

```python
boolean (SeatHasPower) {
  description (Does this seat have a power outlet?)
}

decimal (CurrencyValue) {
  description (The value part of the currency.)
}

enum (Season) {
  description (Names of the seasons)
  symbol (Spring)
  symbol (Summer)
  symbol (Autumn)
  symbol (Winter)
}

integer (Quantity) {
  description (How many to buy.)
}

name (BusinessName) {
  description (The name of a business.)
}

qualified (PhoneNumber) {
  description (A string representing a phone number.)
  regex-pattern ("\\+?1? ?-? ?((\\(\\d\\d\\d\\))|\\d\\d\\d)? ?-? ?\\d\\d\\d ?-? ?\\d\\d\\d\\d")
}

text (MapUrl) {
  description (Contains an URL to a map of the business)
  extends (entity.EntityUrl)
}
```

- Structure : C언어의 구조체와 같은 형식
  - Primitive 타입들을 묶어서 하나의 객체로서 사용하는 타입
  - C의 구초체와 비슷한 역할



---



## :baby_chick: 4. Business Logic 구현

### :hatching_chick: 4.1 ​Java Script 기초와 Bixby Business Logic 구현

#### 	4.1.1 Javascript 기초

**Bixby에서 사용되는 Javascript**

함수도 객체이다! 변수를 저장하고 다른 객체에서 변수처럼 사용가능!

- Module.expots: 다른 파일에서 해당 함수 혹은 값이 사용될 수 있도록 모듈화 하는 함수

- Require: Module.exports의 저장 값을 가져오는 함수

- 변수 : 데이터를 저장하는 저장소

  - var : 전체 외부 함수까지 사용 할 수 있는 유효범위
  - const : 블록 유효 범위를 갖는 변수, let 과 다른 점은 한번 할당된 값은 변경 불가
  - let : 블록 유효 범위를 갖는 변수, const와 다른 점은 할당된 값의 변경 가능

- 분기

  - if 문

- 루프 

  - for 문

  #### 

  Action 과 



---

#### 	4.1.2 Bixby Business Logic

**Bixby Business Logic**

Action과 Javascript

- Action과 Javascript 파일은 1:1 매칭

- Action의 input은 Javacript 함수의 parameter

- Action의 output은 Javascript 함수의 return 값

- Endpoints : Action과 리소스를 매핑시켜주는 설정

  - Local : Action과 로컬 리소스를 매핑
  - Remote: Action과 외부 리소스를 매핑
  - endpoint doc 참조

  ##### 4.2.2 Bixby에서 사용가능한 내장 API

- Config : Capsule의 configuration 정보를 가져옴

  - Capsule.properties

- Console: Debug Console에 로그를 찍을 때  사용

- Dates: 날짜 관련 함수를 제공

- Fail: Runtime 에러 exception을 핸들링

- http: http request를 위한 함수를 제공

- secret: Capsule의 secrets를 가져옴

  - 빅스비 센터 Teams& Capsule >> Config & Secrets >> Secrets 에 key를 안전하게 보관.

   

---

### :hatching_chick: 4.2 시나리오를 통한 Action, Concept, Business Logic 구현

예시 시나리오: 특정장소에 있는 가게 찾기

​	발화 : 수원시에 있는 상점 찾아줘

​	캡슐의 액션이 필요 : 상점찾기

​	데이터에서 수원에 있는 상점 정보 불러오기





## :baby_chick: ​6. Bixby Capsule Endpoints

### :hatching_chick: 6.1 Bixby Casule Endpoints

#### 6.1.1 Endpoints 개요

​	**EndPoints란?**

모델링한 Acion과 Business Logit을 연결해 주는 역할

Bixby Language 구현

​	**Enpoints의 종류**

- Local Endpoint
- Remote Endpoint



#### 6.1.2 Enpoints의 종류

- Local Endpoints
  - 캡슐 내부의 리소스나 코드를 사용하는 형태
  - 발화에 알맞는 내부의 자바스크립트 코드를 찾아서 결과를 반환
- Remote Endpoint
  - 빅스비 내부 캡슐을 거치지 않고, 직접 API를 호출하여 결과를 반환
- 예시

![Endpoints 예시](https://user-images.githubusercontent.com/52685322/65817657-079f1e00-e245-11e9-9570-b3d3181a3f13.jpg)



### :hatching_chick: 6.2  Bixby Capsule로 외부서버 연동하기

#### 6.2.1 Remote Endpoints

- 직접 API 서버를 연동, 따로 빅스비캡슐의 모델링에 대응 하는 비지니스 로직을 작성할 필요 x
- API서버를 가져오는 OUPUT 컨솔은 필요



#### 6.2.2 JavaScript HTTP

