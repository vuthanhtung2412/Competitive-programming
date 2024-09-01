package main

import (
	"fmt"
	"unsafe"
)

func main() {
	fmt.Println("this is a test")
	testFloat()
}

func capVsSize() {
	arr1 := make([]int, 5)
	fmt.Println(len(arr1))
	fmt.Println(cap(arr1))
	arr2 := make([]int, 0, 5)
	fmt.Println(len(arr2))
	fmt.Println(cap(arr2))
}

func slicingArray() {
	a := make([]int, 5)
	subA := a[3:]
	fmt.Printf("%p\n", &a[0])
	fmt.Printf("%p\n", &subA[0])
	// Get the pointers to the first elements of a and subA
	ptrA := unsafe.Pointer(&a[0])
	ptrSubA := unsafe.Pointer(&subA[0])

	// Convert the pointers to uintptr for arithmetic
	addressA := uintptr(ptrA)
	addressSubA := uintptr(ptrSubA)

	fmt.Println(addressSubA - addressA) // facilitate reading the difference of hexadecimal address
}

func testFloat() {
	fmt.Println(float64(1+2) / 2)
}
