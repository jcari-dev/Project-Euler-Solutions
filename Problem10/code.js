let checkPrime = (n) =>{

    let result = true

    for(let y = 2; y <= Math.sqrt(n); y++){

        if(n % y === 0){
            result = false;
            break;
        }

    }

    return result
}


let findPrimeSum = (num) =>{


    let arrayOfPrimes = []

    for(let x = 2; x < num; x++){

        if(checkPrime(x)){
            arrayOfPrimes.push(x)
        }
    }

    let sumOfPrimes = arrayOfPrimes.reduce((a, b) => a + b, 0)

    return sumOfPrimes

}

console.log(findPrimeSum(2000000))