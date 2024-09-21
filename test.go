package main

import (
	"fmt"
	"sort"
	"unsafe"
)

func main() {
	fmt.Println("this is a test")
	customSort()
}

func capVsSize() {
	arr1 := make([]int, 5)
	fmt.Println(len(arr1))
	fmt.Println(cap(arr1))
	arr2 := make([]int, 0, 5)
	fmt.Println(len(arr2))
	fmt.Println(cap(arr2))
}

func sliceMemAddress() {
	a := make([]int, 5)
	subA := a[3:]
	fmt.Printf("%p\n", &a[0])
	fmt.Printf("%p\n", &subA[0])
	arrAsParam(subA)
	// Get the pointers to the first elements of a and subA
	ptrA := unsafe.Pointer(&a[0])
	ptrSubA := unsafe.Pointer(&subA[0])

	// Convert the pointers to uintptr for arithmetic
	addressA := uintptr(ptrA)
	addressSubA := uintptr(ptrSubA)

	fmt.Println(addressSubA - addressA) // facilitate reading the difference of hexadecimal address
}

func arrAsParam(a []int) {
	fmt.Printf("%p\n", &a[0])
}

func testFloat() {
	fmt.Println(float64(1+2) / 2)
}

func arrayPartition() {
	a := make([]int, 5)
	for i := range a {
		a[i] = i
	}
	fmt.Println(a[0:0])
	fmt.Println(a[1:4])
	fmt.Println(a[0:5])
	fmt.Println(a[5:])
	fmt.Println(a[0:1])
	b := make([]int, 0, 3)
	fmt.Println(b[:0])
	fmt.Println(b[0:])
}

func emptySliceHeader() {
	var arr []int
	fmt.Println(len(arr))
	fmt.Println(cap(arr))
	arr = append(arr, 2)
	fmt.Println(arr)
}

func MTArrayInMap() {
	var m map[int][]int
	a, _ := m[0]
	fmt.Println(a)
	a = append(a, 0)
	fmt.Println(m[0])
}

func customSort() {
	type Person struct {
		Name string
		Age  int
	}

	// Slice of structs
	people := []Person{
		{"Alice", 30},
		{"Bob", 25},
		{"Charlie", 35},
		{"Dave", 25},
	}

	// Sort by Age (ascending), and if Ages are equal, by Name (alphabetical order)
	sort.Slice(people, func(i, j int) bool { // if true i index come first
		if people[i].Age == people[j].Age {
			return people[i].Name < people[j].Name // Sort by Name if Age is equal
		}
		return people[i].Age < people[j].Age // Sort by Age
	})

	// Print the sorted slice
	fmt.Println("Sorted people:", people)
}
