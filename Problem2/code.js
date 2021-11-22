let fib = (n, memo = []) =>{
    if(memo[n] != null){
        return memo[n]
    }

    let result
    if( n <= 2){
        result = 1
    } else {
        result = fib(n - 1, memo) + fib(n - 2, memo)
    }
    memo[n] = result

    return result
}

let x = 0

let evenFibs = []

while(fib(x) < 4000000){
    if(fib(x) % 2 === 0){
        evenFibs.push(fib(x))
    }
    x++
}

let evenFibsSum = evenFibs.reduce((a, b) => a + b, 0)

console.log(evenFibsSum)