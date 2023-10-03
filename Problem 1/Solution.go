package main

import "fmt"

func fizzBuzzSum(upTo int) {
	sum := 0
	for i := 0; i < upTo; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i

		}
	}

	fmt.Println(sum)
}

func main() {
	fizzBuzzSum(1000) // 233168
}
