let findMultiplesOfThreeAndFiveUnder = (number) =>{

    let multiplesOfThreeAndFive = []

    for(let x = 1; x < number; x++){
        if(x % 3 === 0 || x % 5 === 0){
            multiplesOfThreeAndFive.push(x)
        }
    }

    return multiplesOfThreeAndFive.reduce((a, b) => a + b, 0)

}

console.log(findMultiplesOfThreeAndFiveUnder(1000))