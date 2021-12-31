const _ = require("underscore");

const isPrime = (num) => {
  let response = true;
  if (num <= 1) {
    response = false;
  }
  for (let i = 2, s = Math.floor(Math.sqrt(num)); i <= s; i++)
    if (num % i === 0) {
      response = false;
      break;
    }
  return response;
};

const isPandigital = (num) => {
  let numLength = num.toString().split("").length;
  let numArr = num.toString().split("").map(Number);

  let pandigital = false;
  let contain = 0;
  let digits = _.range(1, numLength + 1);
  let done = [];

  for (let x = 0; x <= digits.length; x++) {
    if (digits.includes(numArr[x]) && !done.includes(numArr[x])) {
      done.push(numArr[x]);
      contain++;
    }
  }

  if (contain === numLength) {
    pandigital = true;
  }

  return pandigital;
};

const checkPandigital = () => {
  let listOfPandigitalPrimes = [];

  let digits = _.range(1, 11);

  let fullPandigital = false;
  let number = 9;
  while (fullPandigital === false) {
    if (isPrime(number)) {
      if (number.toString().split("").length > 11) {
        fullPandigital = true;
        console.log("done");
      }
      if (isPandigital(number)) {
        listOfPandigitalPrimes.push(number);
        console.log(number);
      }
    }
    number++;
  }
  let sortedPandigitalList = Float64Array(listOfPandigitalPrimes);

  sortedPandigitalList = sortedPandigitalList.sort();
  console.log(sortedPandigitalList.reverse());
  return listOfPandigitalPrimes;
};

console.log(checkPandigital());
