package graph

import (
	"fmt"
	"testing"
)

func Test261(t *testing.T) {
	fmt.Println(validTree(5, [][]int{{0, 1}, {0, 2}, {0, 3}, {1, 4}}))
	fmt.Println(validTree(5, [][]int{{0, 1}, {1, 2}, {2, 3}, {1, 3}, {1, 4}}))
	fmt.Println(validTree(5, [][]int{{1, 2}, {3, 4}}))
}

func validTree(n int, edges [][]int) bool {
	// the main point is that there should only be 1 connected component
	// and no loop
	// submited on neetcode
	parents := make([]int, n)
	for i := range parents {
		parents[i] = i
	}

	var find func(i int) int
	find = func(i int) int {
		if parents[i] == i {
			return i
		}
		return find(parents[i])
	}

	var union func(i, j int) bool
	union = func(i, j int) bool { // if looped or not
		pi := find(i)
		pj := find(j)
		if pi == pj {
			return true
		}
		parents[pi] = pj
		return false
	}

	for _, e := range edges {
		if union(e[0], e[1]) {
			return false
		}
	}

	for i := 1; i < n; i++ {
		if find(i) != find(i-1) {
			return false
		}
	}
	return true
}
