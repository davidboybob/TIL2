//var
console.log(a) // undefined => 메모리 미리 확보
var a = 10
console.log(a)


// js 가 이해한 코드
var a
console.log(a) // undefined
a = 10
console.log(a)


//let => 안됨.  ReferenceError: Cannot access 'b' before initialization
console.log(b)
let b = 10
console.log(b)

//마찬가지로 아래와 같은 과정을 거친다.
let b
console.log(b)
b = 10 // 할당 불가 (초기화가 아직 안됨)
console.log(b)
// WHY? 초기화 전에 할당할려고 해서! 



if ( x !== 1 ) {
  console.log(y) // undefined
  var y = 3
  if ( y === 3 ) {
    var x = 1
   }
   console.log(y) // 3
}

if ( x === 1 ) {
  console.log(y) // 3
}

// JS 가 이해한 코드
var x 
var y 

if ( x !== 1 ) {
  console.log(y) // undefined
  var y = 3
  if ( y === 3 ) {
    var x = 1
   }
   console.log(y) // 3
}

if ( x === 1 ) {
  console.log(y) // 3
}