package main

import "fmt"

func main() {
	fmt.Println(nextGreaterElements([]int{1, 2, 1}))
	fmt.Println(nextGreaterElements([]int{1, 2, 3, 4, 3}))
}

type pair struct {
	i, v int
}

func nextGreaterElements(nums []int) []int {
	res := make([]int, len(nums))
	for i := range res {
		res[i] = -1
	}
	s := make([]pair, len(nums))
	var size int
	for i, v := range nums {
		for {
			if size == 0 {
				s[0] = pair{i: i, v: v}
				size++
				break
			}
			if s[size-1].v < v {
				res[s[size-1].i] = v
				size--
			} else {
				s[size] = pair{i: i, v: v}
				size++
				break
			}
		}
	}
	size = 0
	for i, v := range nums {
		for {
			if size == 0 {
				s[0] = pair{i: i, v: v}
				size++
				break
			}
			if s[size-1].v < v {
				res[s[size-1].i] = v
				size--
			} else {
				s[size] = pair{i: i, v: v}
				size++
				break
			}
		}
	}
	return res
}
