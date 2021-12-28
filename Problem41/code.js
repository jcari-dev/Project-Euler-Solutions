const _ = require("underscore")

const isPrime = (num) => {
  let response = true;
  if (num <= 1) {
    response = false;
  }
  for (let i = 2, s = Math.floor(Math.sqrt(num)); i <= s; i++)
    if (num % i === 0) {
      response = false;
    }
  return response;
};

const isPandigital = (num) =>{
  let numLength = num.toString().split("").length

  // console.log(numLength)
  let pandigital = false
  let contain = 0;
  let digits = _.range(1, numLength+1)

  for(let x = 0; x < numLength+1; x++){
    // console.log(digits[x])
    // console.log("x: ", x, "digits[x]: ", digits[x])
    if(digits.includes(x)){
      contain++
    }
  }
  // console.log(contain)
  if(contain === numLength){
    
    pandigital = true
  }

  return pandigital 
}

const checkPandigital = () =>{

  let listOfPandigitalPrimes = [];

  let digits = _.range(1, 11)

  let fullPandigital = false
  let number = 9;
  while(fullPandigital === false){
    if(isPrime(number)){
      if(isPandigital(number)){
        listOfPandigitalPrimes.push(number)
        // console.log(number)
        if(number.toString().split("").length === 11){
          fullPandigital = true
          console.log('done')
        }
      }
    }
    number++
  }
  console.log(listOfPandigitalPrimes)
  return listOfPandigitalPrimes
}

console.log(checkPandigital())

// isPandigital(5432167980)