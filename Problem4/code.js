 // I promise you will need eye surgery after reading this file

 let checkPalindrome = (num) => {
    num = String(num).split("");
  
    let firstHalf = num.slice(0, num.length / 2);
    let secondHalf = num.slice(num.length / 2, num.length);
  
    secondHalf = secondHalf.reverse();
  
    return firstHalf.join("") === secondHalf.join("");
  };
  
  let runPalinChecker = (startingFrom) => {
  
      let response = 0
  
    for (let x = 0; x <= startingFrom; x++) {
      if (checkPalindrome(x * startingFrom)) {
          response = x * startingFrom
      }
    }
  
    return response;
  };
  
  let findLargestPalindromeUsingTheseDigits = (digit) => {
    let startingFrom = new Array(digit).fill(9);
  
    startingFrom = parseInt(startingFrom.join(""));
  
    let largestPalindrome = 0;
  
    while (startingFrom != []) {
      if (runPalinChecker(startingFrom)) {
        if(runPalinChecker(startingFrom) > largestPalindrome){
          largestPalindrome = runPalinChecker(startingFrom)
        }
      }
      startingFrom--;
    }
  
    return largestPalindrome;
  };
  
  console.log(JSON.stringify(findLargestPalindromeUsingTheseDigits(3)));