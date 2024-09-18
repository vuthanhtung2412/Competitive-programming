package pq

import (
	"container/heap"
	"fmt"
	"testing"
)

func Test(t *testing.T) {
	mf := Constructor()
	commands := []string{"addNum", "addNum", "findMedian", "addNum", "findMedian"}
	args := []any{1, 2, nil, 3, nil}
	for i := 0; i < len(commands); i++ {
		exec(&mf, commands[i], args[i])
	}
}

func exec(mf *MedianFinder, command string, arg any) {
	switch command {
	case "addNum":
		mf.AddNum(arg.(int))
	case "findMedian":
		fmt.Println(mf.FindMedian())
	default:
		panic("no operation found")
	}
}

type MedianFinder struct {
	lh MaxHeap // lower half heap
	uh MinHeap // upper half heap
}

func Constructor() MedianFinder {
	return MedianFinder{
		lh: MaxHeap{},
		uh: make(MinHeap, 0),
	}
}

func (mf *MedianFinder) AddNum(num int) {
	// add to the correct half
	if mf.uh.Len() == 0 || num >= mf.uh[0] { // Upper half container 1 element more in case of uneven #element
		heap.Push(&mf.uh, num)
	} else {
		heap.Push(&mf.lh, num)
	}
	// Balance 2 half
	if (mf.lh.Len()+mf.uh.Len())%2 == 0 {
		if mf.lh.Len() > mf.uh.Len() {
			heap.Push(&mf.uh, heap.Pop(&mf.lh))
			return
		}
		if mf.lh.Len() < mf.uh.Len() {
			heap.Push(&mf.lh, heap.Pop(&mf.uh))
			return
		}
		return
	}

	if (mf.lh.Len()+mf.uh.Len())%2 == 1 {
		if mf.lh.Len() > mf.uh.Len() {
			heap.Push(&mf.uh, heap.Pop(&mf.lh))
			return
		}
	}
}

func (mf *MedianFinder) FindMedian() float64 {
	if mf.lh.Len()+mf.uh.Len() == 0 {
		return 0
	}
	if (mf.lh.Len()+mf.uh.Len())%2 == 0 {
		return (float64(mf.lh[0]) + float64(mf.uh[0])) / 2
	}
	return float64(mf.uh[0])
}

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
