// 변수 지정

// let x =1
// undefined
// x
// 1
// let x = 2
// VM124:1 Uncaught SyntaxError: Identifier 'x' has already been declared
//     at <anonymous>:1:1
// (anonymous) @ VM124:1
// x = 3
// 3
// 할당과 선언  => 블락 유효처리 

// // let (변수)
// let x = 1
// if (x === 1) { 
//   let x = 2

//   console.log(x) // 2
// }
// console.log(x) // 1

// // const 정수

// // const 선언시에 후기 값을 생략하면 오류바생
// const MY_FAV


// // =>
// const MY_FAV = 7
// console.log('my faviorite numbrer is:' + MY_FAV)
// // 상수를 재할당 하려는 시도는 오류 발생.
// //MY_FAV = 20
// //const MY_FAV = 20
// // let MY_FAV = 20
// // var MY_FAV = 20


// if (MY_FAV === 7) {
//   //  블록 유효 범위로 지정된 MY_FAV 이라는 변수를 만드므로 괜찮다.
//   // 즉, 전역이 아닌 범위안이므로 읾 공간에서 출동이 나지 않는다.
//   const MY_FAV = 20
  
//   console.log('my faviorite number is' + MY_FAV) // 20
// }

// console.log(MY_FAV) // 7



// //var (변수)

// function varTest() {
//   var x = 1
//   if (true) {
//     var x = 2
//     console.log(x) // 2
//   }
//   console.log(x) // 2
// }

// varTest()


//let 과 var

var a = 1
let b = 2

if (a === 1) {
  var a = 11
  let b = 22

  console.log(a) // 11
  console.log(b) // 22
}

console.log(a) // 11
console.log(b) // 2


// 식별자 작성 스타일
//1. 카멜 케이스(camelCase) - 객체, 변수, 함수(=== lower-camel-case)
let dog
let variableName

// 배열은 복수형 변수명을 사용
const dogs = []

//정규 표현식은 'r'로 시작
const rDecs = /.*/

//함수
function getPropertyName() {
  return 1
}

// boolean 을 반환하는 변수나 함수 - 'is'로 시작
let isAvailable = false

//2. 파스칼 케이스 (PascalCase) - 클래스, 생성자 ( === upper-camel-case)

class User {
  constructor(options) {
    this.name = option.name
  }
}

// 3. 대문자 스네이크 케이스 (SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = '&DFJ#F(DFJD*FYDF&DNF&DMD^FBD%FGD$FG#J@JHF'

