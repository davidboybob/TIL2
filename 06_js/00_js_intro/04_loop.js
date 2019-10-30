let i = 0

// while 문
while (i < 6) { // 0~ 5까지 출력됨.
  console.log(i)
  i++
}


//for 문
for (let j =0; j < 6; j++) { //변수정의, 조건정의, 확정조건의 증감식 정의
  console.log(j)
}

const numbers = [0, 1, 2, 3, 4, 5,]

for (let number of numbers) {
  console.log(number)
}

for (let number of [0, 1, 2, 3, 4, 5]) {
  console.log(number)
}

for (const number of [0, 1, 2, 3, 4, 5]) {
  console.log(number)
}

