// https://leetcode.com/problems/sliding-window-maximum/description/
package main

import (
	"errors"
	"fmt"
)

func main() {
	fmt.Println(maxSlidingWindow([]int{1, 3, -1, -3, 5, 3, 6, 7}, 3))
	fmt.Println(maxSlidingWindow([]int{1}, 1))
}

var (
	errEmpty = errors.New("Deque empty")
	errFull  = errors.New("Deque full")
)

type Pair struct {
	id  int
	val int
}

type Deque struct {
	items []Pair
	head  int
	size  int
}

func NewDeque(size int) Deque {
	return Deque{
		items: make([]Pair, size),
	}
}

func (d *Deque) PushFront(p Pair) error {
	if d.size == cap(d.items) {
		return errFull
	}
	d.items[d.head] = p
	d.head = (d.head + 1) % cap(d.items)
	d.size++
	return nil
}

func (d *Deque) PopFront() (Pair, error) {
	res, err := d.PeekFront()
	d.size--
	d.head = (cap(d.items) + d.head - 1) % cap(d.items)
	return res, err
}

func (d *Deque) PopBack() (Pair, error) {
	res, err := d.PeekBack()
	d.size--
	return res, err
}

func (d *Deque) PeekFront() (Pair, error) {
	if d.size == 0 {
		return Pair{}, errEmpty
	}
	return d.items[(cap(d.items)+d.head-1)%cap(d.items)], nil
}

func (d *Deque) PeekBack() (Pair, error) {
	if d.size == 0 {
		return Pair{}, errEmpty
	}
	return d.items[(cap(d.items)+d.head-d.size)%cap(d.items)], nil
}

func trackMax(d *Deque, i int, val int) {
	for {
		if d.size == 0 {
			d.PushFront(Pair{
				id:  i,
				val: val,
			})
			break
		}
		p, err := d.PeekFront()
		if err != nil {
			panic(err)
		}
		if val > p.val {
			d.PopFront()
		} else {
			d.PushFront(Pair{
				id:  i,
				val: val,
			})
			break
		}
	}
}
func maxSlidingWindow(nums []int, k int) []int {
	res := make([]int, 0, len(nums)-k+1)
	d := NewDeque(k)
	// Initialize Deque
	for i := 0; i < k; i++ {
		trackMax(&d, i, nums[i])
	}
	p, err := d.PeekBack()
	if err != nil {
		panic(err)
	}
	res = append(res, p.val)
	// Window sliding
	for i := k; i < len(nums); i++ {
		p, err := d.PeekBack()
		if err != nil {
			panic(err)
		}
		if i-k == p.id {
			d.PopBack()
		}
		trackMax(&d, i, nums[i])

		p, err = d.PeekBack()
		if err != nil {
			panic(err)
		}
		res = append(res, p.val)
	}

	return res
}
