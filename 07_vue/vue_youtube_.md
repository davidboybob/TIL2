단방향 데이터 흐름의 ㅊ이점

1. vue app의 데이터 흐름을 쉽게 파악할 수 있음.
2. 부모 컴포넌트에서 업데이트가 일어나면 자식컴포넌트는 자동 업데이트( 즉, 자식 컴포넌트의 상태를 관리하지 않아도 된다.)
3. 하위 컴포넌트가 실수로 부모의 상태를 변경하려 app 데이터의 흐름을 추론하기 어렵게 만드는 것을 방지할 수 있다.



- 상위로 데이터를 올려 보낼 때는 Event를 발생시키는 방법을 사용한다. (`emit`)

- `props`는 배열, 객체, 함수 등 무엇이든 내려보내는 **속성(properties)**이고, `emit event`는 자식에서 부모로 **이벤트를 발생** 시키는 것

  

### 정리 SearchBar ==> App

1. 트리거 : input 값 변경(@input)
   - 인자 : event
   - 실행 함수 : onInput
2. 트리거 : input 내 #emit(inputChange)
   - 인자 : 변경된값
   - 실행 함수 : onInputChange





### 흐름

---

사용자가 검색어 입력(SearchBar)

=> 검색 결과를 App.vue로 올려줌





---

### SearchBar

1. 사용자가 input에 값을 입력하면 onInput 함수가 실행
2. inputChange 이벤트와 사용자가 입력한 value 가 함께 상위 컴포넌트인 App.vue로 event와 input value가 emit 된다.

### App

3. SearchBar에서 넘어온 이벤트 inputChange로 인해 onInputChange 함수가 실행된다.
4. onInputChange 함수는 유투브 api 에 요청을 보내고 비디오 리스트를 응답받는다.





console.developers.google.com/

