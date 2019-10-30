const concat = function(str1, str2) {
  console.log(`${str1} - ${str2}`)
  return `${str1} - ${str2}`
}

const check_long_str = function(string) {
  if (string.length > 10) {
      return true
  } else {
      return false
  }
}

if (check_long_str(concat('Happy', 'Hacking'))) {
  console.log('LONG STRING')
} else {
  console.log('SHORT STRING')
}



// function concat(str1, str2) {
//   return `${str1} - ${str2}`
// }

// function check_long_str(string) {
//   if (string.length > 10) {
//       return true
//   } else {
//       return false
//   }
// }

// if (check_long_str(concat('Happy', 'Hacking'))) {
//   console.log('LONG STRING')
// } else {
//   console.log('SHORT STRING')
// }