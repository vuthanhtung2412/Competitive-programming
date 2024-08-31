// https://leetcode.com/problems/trapping-rain-water/
package main

import "fmt"

func main() {
	fmt.Println(trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
	fmt.Println(trap([]int{4, 2, 0, 3, 2, 5}))
}

// waterTrapped[i]=min(maxL[i], maxR[i]) - heigth[i]
func trap(height []int) int {
	maxL := make([]int, len(height))
	maxR := make([]int, len(height))
	tempL := 0
	tempR := 0
	for i := 0; i < len(height); i++ {
		if height[i] > tempL {
			tempL = height[i]
		}
		maxL[i] = tempL
	}
	for i := len(height) - 1; i >= 0; i-- {
		if height[i] > tempR {
			tempR = height[i]
		}
		maxR[i] = tempR
	}
	res := 0
	for i := 0; i < len(height); i++ {
		res += min(maxL[i], maxR[i]) - height[i]
	}
	return res
}
