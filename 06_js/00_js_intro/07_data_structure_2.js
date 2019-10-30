const me = {
  name: 'ssafy', // key가 한 단어 일때
  'phone number': '01023451345', // key가 여러단어 일때
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',

  }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
// console.log(me.phone number) -> 안됨.
console.log(me['phone number']) // key가 여러 단어일 경우 반드시 []로 접근


console.log(me.appleProducts) // { ipad: '2018pro', iphone: '7', macbook: '2019pro' }
console.log(me.appleProducts.ipad) // 2018pro


// Object Literal (객체 표현법)
//ES5 사용법
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers']
}

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)

console.log(bookShop.books[0])


//ES6++ 사용법
//object의 key와 value가 같다면, 마치 배열처럼 한번만 작성 가능.
let bookShopTwo = {
  books,
  comics,
  magazines,
}

console.log(bookShopTwo)

//------------------------------------------------

//JSON
const jsonData = JSON.stringify({ //JSON -> String
  coffee: 'Americano',
  iceCream: 'Mint Choco',

})

console.log(jsonData) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof jsonData) 


const parseData = JSON.parse(jsonData)  // parsing 작업
console.log(parseData) // { coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof parseData) // object