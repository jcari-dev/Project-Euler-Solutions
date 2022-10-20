function factorsOf(n) {
    let factors = [];
    let div = 2;
  
    while (n >= 2) {
      if (n % div == 0) {
        factors.push(div);
        n = n / div;
      } else {
        div++;
      }
    }


    return factors[factors.length-1];
  }

console.log(factorsOf(600851475143)) // 6857


