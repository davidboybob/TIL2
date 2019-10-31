
// 기본틀
const axios = require('axios')

axios.get('http://jaaasonplaceholder.typicode.com/posts')
  .then(response => {console.log(response)})
  .catch(err => {console.log(err)})


