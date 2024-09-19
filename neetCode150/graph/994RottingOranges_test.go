package main

import (
	"fmt"
	"testing"
)

func Test994(t *testing.T) {
	fmt.Println(orangesRotting([][]int{
		{2, 1, 1},
		{1, 1, 0},
		{0, 1, 1},
	}))

	fmt.Println(orangesRotting([][]int{
		{2, 1, 1},
		{0, 1, 1},
		{1, 0, 1},
	}))

	fmt.Println(orangesRotting([][]int{
		{0, 2},
	}))

	fmt.Println(orangesRotting([][]int{
		{2, 2},
		{1, 1},
		{0, 0},
		{2, 0},
	}))
}

func orangesRotting(grid [][]int) int {
	h := len(grid)
	w := len(grid[0])
	goodOrange := map[int]struct{}{}
	q := newDeque(h * w)
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == 1 {
				goodOrange[i*w+j] = struct{}{}
			}
			if grid[i][j] == 2 {
				q.pushBack(i*w + j)
			}
		}
	}

	toBQ := newDeque(h * w) // necessary for iteration by iteration scan
	res := 0
	for {
		if q.len == 0 && toBQ.len == 0 {
			break
		}

		if q.len == 0 {
			q, toBQ = toBQ, q
			res++
		}

		o, err := q.popFront()
		if err != nil {
			panic("stupid")
		}

		r, c := o/w, o%w
		// process
		delete(goodOrange, o)

		// add adjacent cell to the queue
		for _, d := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
			nr := r + d[0] // neighbor row
			nc := c + d[1] // neighbor col
			if 0 <= nr && nr < h && 0 <= nc && nc < w && grid[nr][nc] == 1 {
				toBQ.pushBack(nr*w + nc)
				grid[nr][nc] = 2
			}
		}
	}

	if len(goodOrange) > 0 {
		return -1
	}
	return res
}
