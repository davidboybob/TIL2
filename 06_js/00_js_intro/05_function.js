// 1. 선언식 // 2. 표현식


// 1.선언식 (statement, declaration)
// 함수 선언식은 코드가 실행되기 전에 로드된다.
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))


// 2. 표현식 (expression)
// 함수 표현식은 인터프리터가 해당 코드에 도달 했을 때 로드 된다.

const sub = function(num1, num2) {
  return num1 - num2
}

console.log(sub(7, 2))

console.log(typeof add)
console.log(typeof sub)


// Arrow Function 화살표 함수
// 화살표함수의 경우 일반 function 키워드로 정의한 함수와 100% 동일한 것이 아니다.
// 화살표함수는 항상 익명입니다.
// 변수에 할당할 수 있지만, 이름 붙은 함수(생성자)로는 만들 수 없습니다.
// 

const ssafy1 = function(name) {
  return `hello, ${name}`
}

// 리팩토링(refactoring)과정
// 1. function keyword 삭제
const ssafy1 = (name) => { return `hello, ${name}` }

// 2. 인자의 `()` 소괄호 생략 (딘, 함수 매개변수가 하나일 경우만 생략가능)
const ssafy1 = name => { return `hello, ${name}` }

// 3. {} && return 생략 (단, 함수의 바디에 표현식이 1개일 경우만 )
const ssafy1 = name => `hello, ${name}`



// Arrow function refactoring
let square = function(num) {
  return num ** 2
  
}

//1. 
let square = (num) => { return num ** 2 }
//2.
let square = num => { return num ** 2}
//3.
let square = num => num ** 2


//매개 변수가 없다면 ? ()나 _를 사용
let noArgs = () => 'No argumments'
let noArgs = _ => 'No argumments'


// object를 return 한다면,
let returnObject = () => { return {key: 'value'} } // return 을 명시적으로 적어준다. 
console.log(returnObject()) // { key: 'value' }

//object를 return 하는데, return을 사용하지 않을 경우. => 소괄호를 사용.
let returnObject = () => ({key: 'value'})

// object return 시 문제상황
// 1. return 이 없는데 ()를 안 쓴 경우
let returnObject = () => {key: 'value'}
const text = returnObject()
console.log(typeof test) // undefined => return을 제외한다면, 소괄호를 해줘야 한다.

//기본 매개변수를 줄 때는 매개변수의 개수와 상관 없이 무조건 ()를 해야한다. 
const sayHello = (name='noName') => `hi ${name}`

//Anonymous Function (익명함수 / 1회용함수)
// 1. 기명함수로 만들기 (변수/상수에 할당하기) - 생성과 동시에 함수의 인수로 할당하는 방법.
const cube = function (num) { return num ** 3 } // 변수 할당 
const squareRoot = num => num ** 0.5

console.log(cube(2)) // 8
console.log(squareRoot(4)) // 2

// 2. 익명함수 즉시 실행
console.log((function (num) { return num ** 3 })(2))
console.log((num => num ** 0.5)(4))


// 함수 호이스팅
ssafy1()

function ssafy1() {
  console.log('hoistings')
}

//변수에 할당한 함수(표현식)는 호이스팅이 되지 않는다.
// 이것은 변수의 유효범위 규칙을 따르기 때문이다.

ssafy2()
let ssafy2 = function () {
  console.log('hoistings')
}

