//Array Helper Method

//2. .map(callback())
//배열 내의 모든 요소에 대하여 각각 주어진 함수(callback)를 호출한 결과를 모아 새로운 배열 return
//일정한 형식의 배열을 다른 형식으로 바꿔야 할 때 사용한다. 


//for 
var numbers = [1, 2, 3,]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i] * 2)
}

console.log(doubleNumbers)

console.log(numbers) // 원본 유지 


const NUMBERS = [1, 2, 3,]
const DOUBLE_NUMBERS = NUMBERS.map(function(number) {
  return number * 2
})

console.log(DOUBLE_NUMBERS)


//리팩토링
// const DOUBLE_NUMBERS = NUMBERS.map(number => number * 2 )


//2-1 연습
const numbers2 = [4, 9, 13,]
const roots = numbers2.map(Math.sqrt)

console.log(roots)

// 2-2 map을 사용해 images 배열 안의 Object 들의 height 들만 저장되어 있는 heights 배열을 만드시오.
const images = [
  { height: '34px', width: '39px'},
  { height: '12px', width: '11px'},
  { height: '292px', width: '56px'},
  
]

// co`nst heights = images.map(function (image) {
//   return image.height
// })
const heights = images.map(image => image.height)
console.log(heights)


// 2-3 map을 사용해 trips 배열의 값들을 계산해서 속도 값을 저장하는 배열 speeds를 만드시오.
const trips = [
  {distance: 35, time: 10},
  {distance: 90, time: 10},
  {distance: 60, time: 25},  
]

const speeds = trips.map(trip => (trip.distance / trip.time))
console.log(speeds)

// 2 - 4
const brands = ['Marvel', 'DC']
const movies = ['IronMan', 'Batman',]

// [
//   { name: 'Marvel', hero: 'IronMan'},
//   { name: 'DC', hero: 'Batman'},

// ]


const comics = brands.map(function(x, i) {
  return { name: x, hero: movies[i]}
})
//리팩토링
// const comics = brands.map( (x, i) => ({name: x, hero: movies[i]}))

console.log(comics)