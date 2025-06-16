package main

func main() {
	var sum int
	for i := 1; i < 1000; i++ {
		if i%3 == 0 {
			sum += i
		} else if i%5 == 0 {
			sum += i
		}

	}
	println(sum) // 233168
}
