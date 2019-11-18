const a = 13
const b = -3
const c = 3.14 // float
const d = 2.998e8 // 2.998 * 10^8
const e = Infinity
const f = -Infinity
const g = NaN

console.log(a, b, c, d, e, f, g)


const setence1 = 'sentence'
const setence2 = "'sentence'"
const setence3 = `'sentence'`

//backtrick ` 
// 줄바꿈 + 파이썬의 f-string 처럼 사용할 수 있다.(문자열안에 변수 넣을 수 있다.)


// const word = "안녕
// 하세요."
// console.log(word)

const word1 = "안녕 \n하세요."
console.log(word1)

const word2 = `안녕
하세요.`
console.log(word2)


//Template Literal
// JS 에서 문자열을 입력하는 방식.
const age = 10
const message = `홍길동은 ${age}세 입니다.`
console.log(message)



const happy = 'hello'
const hacking = 'world!!' + 'lol' + '!!!'

console.log(happy, hacking)

// boolean => true, flase 소문자에 주의

// Number.isNaN() 함수는 값이 NaN ㅣ인자
//주어진 값의 유형이 Number 이고 값이 NaN 이면 true
// 아니면 false
Number.isNaN(null) // false
Number.isNaN(undefined)


console.log(Number.isNaN(1 + null)) // false (숫자)
console.log(Number.isNaN(1 + undefined)) // true (숫자가 아님)



console.log(Number.isNaN(NaN)) //true
console.log(Number.isNaN(Number.NaN)) //true
console.log(Number.isNaN(0 / 0)) // true