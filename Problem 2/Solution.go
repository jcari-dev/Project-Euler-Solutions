package main

import "fmt"

func main() {
	solution := 0

	a := 1
	b := 2

	i := 0
	for {
		if a%2 == 0 {
			solution += a
		}

		temp := a
		a = b
		b = temp + a

		i++

		if a > 4000000 {
			break
		}
	}

	fmt.Println(solution) //4613732

}
