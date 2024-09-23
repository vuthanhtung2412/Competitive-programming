package main

import "testing"

func Test77(t *testing.T)

func combine(n int, k int) [][]int {
	res := [][]int{}
	// C(n,r) = n!/(r!(n-r)!)
	// Example
	// combine(4,2) = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
	// combine(4,3) = [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
	// Combine(5,3) = [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
	// Recursive relation : combine(n,k) = prefix([1],(offset(1,combine(n-1,k-1)))) + offset(1,combine(n-1,k))
	// Time complexity : O(n*k*C(n,k)*k)

	// TODO

	return res
}
