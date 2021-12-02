let collatzSequence = (num, count) =>{

    if(num === 1){
      return count
    }
    if(num % 2 === 0){
      count++
      return collatzSequence(num / 2, count)
    } else {
      count++
  
      return collatzSequence(num * 3 + 1, count)
    }
  
  }
  
  let largestCollatz = (under) => {
  
  let largestSequence = [0,0];
  let currentSequence = 0;
  
  for(let x = 1; x < under; x++){
  
  currentSequence = collatzSequence(x, 0)
  
   if(currentSequence > largestSequence[0]){
     largestSequence[0] = currentSequence
     largestSequence[1] = x
   }
  
  }
  
  return largestSequence
  
  }
  
  console.log(largestCollatz(1000000))