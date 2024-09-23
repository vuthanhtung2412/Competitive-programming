package main

import (
	"fmt"
	"slices"
	"testing"
)

func Test77(t *testing.T)

func combine(n int, k int) [][]int {
	// Time complexity : O(k*C(n,k))
	// Because we have C(n,k) choice and take k times to copy to res
	// C(n,k) is often simplified to 2^n
	res := [][]int{}
	curr := []int{}
	deps := 0
	var rec func(i int)
	rec = func(i int) {
		fmt.Printf("%d , %d \n", i, deps)
		deps++
		curr = append(curr, i)
		if deps == k {
			res = append(res, slices.Clone(curr))
		} else {
			for j := i + 1; j <= n; j++ {
				rec(j)
			}
		}
		curr = curr[:len(curr)-1]
		deps--
	}

	for i := 1; i <= n-k+1; i++ {
		rec(i)
	}
	return res
}
