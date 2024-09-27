package main

import "fmt"

func main() {
	fmt.Println(SumSlices([]int{1, 2, 3, 4}, []int{5, 5})) // 20
}

// SumSlices takes two slices of integers, sums them up concurrently using goroutines,
// and returns the total sum.
func SumSlices(slice1, slice2 []int) int {
	s1 := make(chan int)
	go func() { s1 <- sumSlice(slice1) }()
	s2 := make(chan int)
	go func() { s2 <- sumSlice(slice2) }()
	a1 := <-s1
	a2 := <-s2
	return a1 + a2
}

func sumSlice(slice []int) int {
	sum := 0
	for _, v := range slice {
		sum += v
	}
	return sum
}
