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

let giveMePrimeN = (num) => {
  let count = 0;
  let n = 2;
  let arrOfPrimes = [];
  while (count < num) {
    if (isPrime(n)) {
      count++;
      arrOfPrimes.push(n);
    }
    n++;
  }

  return [arrOfPrimes, arrOfPrimes[arrOfPrimes.length-1]];
};

console.log(giveMePrimeN(10001));
