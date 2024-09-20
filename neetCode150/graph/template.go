package main

import "errors"

var (
	errEmpty = errors.New("empty")
	errFull  = errors.New("full")
)

type deque struct {
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
	if d.len == len(d.items) {
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
