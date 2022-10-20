let SumSquareDiff = (num) => {
  let array = [...Array(num + 1).keys()];
  let LengthOfArray = array.length;

  let arrayOfSquares = [];
  let sumOfArray = array.reduce((a, b) => a + b, 0);

  for (let x = 0; x < LengthOfArray; x++) {
    arrayOfSquares.push(Math.pow(array[x], 2));
  }
  let SquaredSumOfArray = Math.pow(sumOfArray, 2);
  let sumOfSquaredArrays = arrayOfSquares.reduce((a, b) => a + b, 0);
  return [
    sumOfSquaredArrays,
    SquaredSumOfArray,
    SquaredSumOfArray - sumOfSquaredArrays,
  ];
};

console.log(SumSquareDiff(100));
