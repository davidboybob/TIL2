vue.js

SPA

페이지 변경이 없고, vue.js

보간법

 인터폴레이션 {{  }}



html은 뷰를 위한 껍데기 역할

---

el: => 엘리멘트

## 인스턴스 옵션

1. el
   - Vue 인스턴스와 DOM을 연결(마운트, mount) 하는 옵션
   - View - View Model을 연결 시킨다.
   - HTML의 id나 class와 마운트가 가능하다.
2. data
   - Vue 인스턴스의 데이터 객체, 인스턴스의 `속성`이라고도 부름
   - 데이터 객체는 반드시 기본 객체 `{ }` 이어야 함.
   - 객체 내부의 아이템들은 value로써 모든 타입의 객체를 가질수 있다. (object, string, integer array ...)
   - 정의된 속성은 인터폴레이션 (`{{  }}`) 을 통해서 View 에서 렌더링 가능
   - data에서도 이벤트리스너와 비슷한 이유로 화살표 함수를 작성해서는 안된다.

---

## methods

- Vue 인스턴스에 추가할 메소드들을 정의하는 곳
- (주의) 메소드를 정의하는 데에 화살표함술르 사용해서는 안된다.





### Vue directive(지시문)

- 디렉티브는 `v-` 접두사가 있는 특수 속성(arrt)이며, 디렉티브 속성의 값은 단일 JS 표현식





### v-for

### v-if

- 특정 조건을 만족할 때만 보여지도록(렌더링되도록)할 수 있다.
- `v-else`는 반드시 v-if 엘리먼트 바로 뒤에 와야 인식 가능.
- `v-elseif`도 존재.



우선순위

- 동일한 노드에서는 v-for가 v-if 보다 높은 우선순위를 가짐.
- 즉, v-if는 루프가 반복될 때마다 실행!(일부 항목만 렌더링 할 때 유용)



### v-on

- JS에서 이벤트리스너랑 비슷한 역할을 함.
- 이벤트 리스너는 HTML element를 querySelector로 가져와 이벤트를 붙여줬다면, Vue는 HTML elemetn 자체에 이벤트를 붙여준다.
- `v-on`: 뒤에 오는 친구를 `전달인자`라고 한다.
- `:`을 붙여 사용하는, 디렉티브 바로 뒤에 붙는 친구들을 지칭한다.



사용법 2가지

1. inline
2. method정의