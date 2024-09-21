package main

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test417(t *testing.T) {
	cs := []struct{ heights, expected [][]int }{
		{
			heights:  [][]int{{1, 2, 2, 3, 5}, {3, 2, 3, 4, 4}, {2, 4, 5, 3, 1}, {6, 7, 1, 4, 5}, {5, 1, 1, 2, 4}},
			expected: [][]int{{0, 4}, {1, 3}, {1, 4}, {2, 2}, {3, 0}, {3, 1}, {4, 0}},
		},
		{
			heights:  [][]int{{1}},
			expected: [][]int{{0, 0}},
		},
	}
	for i, c := range cs {
		t.Run(strconv.Itoa(i), func(t *testing.T) {
			actual := pacificAtlantic(c.heights)
			fmt.Println(actual)
			assert.True(t, compareListPermutated(actual, c.expected, len(c.heights[0])))
		})
	}
}

func compareListPermutated(l1, l2 [][]int, w int) bool {
	if len(l1) != len(l2) {
		return false
	}
	s1 := map[int]struct{}{}

	for _, e := range l1 {
		s1[e[0]*w+e[1]] = struct{}{}
	}

	for _, e := range l2 {
		if _, ok := s1[e[0]*w+e[1]]; !ok {
			return false
		}
	}

	return true
}

func pacificAtlantic(heights [][]int) [][]int {
	h := len(heights)
	w := len(heights[0])
	flowToPA := make([][][2]bool, h) // flow to pacific / alantic
	for i := range flowToPA {
		flowToPA[i] = make([][2]bool, w)
	}

	// dfs Pacific
	var dfsPA func(i, j int, p bool) // p : if we are dfs pacific flow or not
	dfsPA = func(i, j int, p bool) {
		for _, d := range [][2]int{{0, -1}, {-1, 0}, {0, 1}, {1, 0}} {
			pa := 0
			if !p {
				pa = 1
			}
			if 0 <= i+d[0] && i+d[0] < h &&
				0 <= j+d[1] && j+d[1] < w &&
				flowToPA[i+d[0]][j+d[1]][pa] != true &&
				heights[i][j] <= heights[i+d[0]][j+d[1]] {
				flowToPA[i+d[0]][j+d[1]][pa] = true
				dfsPA(i+d[0], j+d[1], p)
			}
		}
	}

	// dfs pacific flow
	for i := range heights {
		flowToPA[i][0][0] = true
		dfsPA(i, 0, true)
	}

	for i := range heights[0] {
		flowToPA[0][i][0] = true
		dfsPA(0, i, true)
	}

	// dfs alantic flow
	for i := range heights {
		flowToPA[i][w-1][1] = true
		dfsPA(i, w-1, false)
	}

	for i := range heights[0] {
		flowToPA[h-1][i][1] = true
		dfsPA(h-1, i, false)
	}

	// return result
	res := [][]int{}
	for i := range flowToPA {
		for j := range flowToPA[0] {
			if flowToPA[i][j][0] && flowToPA[i][j][1] {
				res = append(res, []int{i, j})
			}
		}
	}

	return res
}
