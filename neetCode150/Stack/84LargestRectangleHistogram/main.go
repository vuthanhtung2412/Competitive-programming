package main

import "fmt"

func main() {
	fmt.Println(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}))
	fmt.Println(largestRectangleArea([]int{2, 4}))
}

type pair struct {
	i, v int
}

// Main idea
// max((nextSmaller[i] - prevSmaller[i]) * heights[i] for i in range len
func largestRectangleArea(heights []int) int {
	prevS := make([]int, len(heights))
	nextS := make([]int, len(heights))
	for i := range heights {
		prevS[i] = -1
		nextS[i] = len(heights)
	}
	s := make([]pair, len(heights))
	size := 0
	// Fill next smaller height
	for i, v := range heights {
		for {
			if size == 0 {
				s[0] = pair{i: i, v: v}
				size++
				break
			}
			if s[size-1].v > v {
				nextS[s[size-1].i] = i
				size--
			} else {
				s[size] = pair{i: i, v: v}
				size++
				break
			}
		}
	}
	// Fill previous smaller height
	size = 0
	for i := len(heights) - 1; i >= 0; i-- {
		v := heights[i]
		for {
			if size == 0 {
				s[0] = pair{i: i, v: v}
				size++
				break
			}
			if s[size-1].v > v {
				prevS[s[size-1].i] = i
				size--
			} else {
				s[size] = pair{i: i, v: v}
				size++
				break
			}
		}
	}
	res := -1
	for i := range heights {
		tmp := (nextS[i] - prevS[i] - 1) * heights[i]
		if tmp > res {
			res = tmp
		}
	}
	return res
}
