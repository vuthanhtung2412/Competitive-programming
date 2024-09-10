package main

import (
	"container/heap"
	"fmt"
	"math"
)

func main() {
	fmt.Println(kClosest([][]int{{1, 3}, {-2, 2}}, 1))
	fmt.Println(kClosest([][]int{{3, 3}, {5, -1}, {-2, 4}}, 2))
}

type MaxHeap [][]int

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
	return math.Pow(float64(h[i][0]), 2)+math.Pow(float64(h[i][1]), 2) > math.Pow(float64(h[j][0]), 2)+math.Pow(float64(h[j][1]), 2)
}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.([]int))
}

func (h *MaxHeap) Pop() any {
	// When heap.Pop() is called:
	// The root element (minimum) is swapped with the last element in the array.
	// The last element (which is now at the root) is removed from the slice.
	// The heap is restructured by calling heapify to maintain the heap property.

	// This make more sense that *h = old[1:], since it preserve the cap of the array
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kClosest(points [][]int, k int) [][]int {
	q := make(MaxHeap, k)
	copy(q, points[:k])
	heap.Init(&q)
	// If furthest point of k points > current point
	// Pop the furthest point and add it to the heap
	for _, p := range points[k:] {
		if math.Pow(float64(q[0][0]), 2)+math.Pow(float64(q[0][1]), 2) > math.Pow(float64(p[0]), 2)+math.Pow(float64(p[1]), 2) {
			heap.Pop(&q)
			heap.Push(&q, p)
		}
	}
	return q
}
