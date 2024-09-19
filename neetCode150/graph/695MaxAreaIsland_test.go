package graph

import (
	"errors"
	"fmt"
	"testing"
)

func Test695(t *testing.T) {
	fmt.Println(maxAreaOfIsland([][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}))

	fmt.Println(maxAreaOfIsland([][]int{
		{0, 0, 1, 1},
		{0, 0, 1, 0},
	}))

}

func maxAreaOfIsland(grid [][]int) int {
	h := len(grid)
	w := len(grid[0])

	res := 0
	visited := map[int]struct{}{}
	q := newDeque(h * w)

	var bfs func(i, j int)
	bfs = func(i, j int) {
		a := 0
		q.pushBack(w*i + j)
		for {
			cell, err := q.popFront()
			if err != nil {
				break
			}
			r, c := cell/w, cell%w

			// skip visited cell and water (0 cell)
			_, ok := visited[cell]
			if ok || grid[r][c] == 0 {
				continue
			}

			// process and visit
			a++
			visited[cell] = struct{}{}

			// add adjacent cell to the queue
			for _, d := range [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
				nr := r + d[0] // neighbor row
				nc := c + d[1] // neighbor col
				if _, ok := visited[nr*w+nc]; 0 <= nr && nr < h && 0 <= nc && nc < w && !ok {
					q.pushBack(nr*w + nc)
				}
			}
		}

		if res < a {
			res = a
		}
	}

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == 0 {
				continue
			}
			bfs(i, j)
		}
	}

	return res
}

var (
	errFull  = errors.New("deque full")
	errEmpty = errors.New("deuqe empty")
)

type deque struct {
	// head (front) and tail (back)
	items []int
	head  int
	len   int
}

func newDeque(size int) deque {
	return deque{
		items: make([]int, size),
	}
}

func (d *deque) pushBack(num int) error {
	if len(d.items) <= d.len {
		return errFull
	}
	d.items[(d.head+d.len)%len(d.items)] = num
	d.len++
	return nil
}

func (d *deque) popFront() (int, error) {
	if d.len == 0 {
		return 0, errEmpty
	}
	res := d.items[d.head]
	d.head = (d.head + 1) % len(d.items)
	d.len--
	return res, nil
}
