package main

import "fmt"

func main() {
	fmt.Println("this is a test")
	capVsSize()
}

func capVsSize() {
	arr1 := make([]int, 5)
	fmt.Println(len(arr1))
	fmt.Println(cap(arr1))
	arr2 := make([]int, 0, 5)
	fmt.Println(len(arr2))
	fmt.Println(cap(arr2))
}
