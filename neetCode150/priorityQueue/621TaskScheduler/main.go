package main

import (
	"container/heap"
	"errors"
	"fmt"
)

func main() {
	fmt.Println(leastInterval([]byte{'A', 'A', 'A', 'B', 'B', 'B'}, 2))      // 8
	fmt.Println(leastInterval([]byte{'A', 'C', 'A', 'B', 'D', 'B'}, 1))      // 6
	fmt.Println(leastInterval([]byte{'A', 'A', 'A', 'B', 'B', 'B'}, 3))      // 10
	fmt.Println(leastInterval([]byte{'A', 'C', 'A', 'B', 'D', 'B', 'A'}, 1)) // 6
}

var (
	errEmpty = errors.New("empty")
	errFull  = errors.New("full")
)

// The bigger number of rep more priority
type Task struct {
	val          byte
	rep          int
	lastExecuted int
}

type Deque struct {
	tasks []*Task
	len   int
	head  int
}

func newDeque(size int) Deque {
	return Deque{
		tasks: make([]*Task, size),
	}
}

func (d *Deque) peekBack() (*Task, error) {
	if d.len == 0 {
		return nil, errEmpty
	}
	return d.tasks[(len(d.tasks)+d.head-d.len)%len(d.tasks)], nil
}

func (d *Deque) popBack() (*Task, error) {
	if d.len == 0 {
		return nil, errEmpty
	}
	res := d.tasks[(len(d.tasks)+d.head-d.len)%len(d.tasks)]
	d.len -= 1
	return res, nil
}

func (d *Deque) pushFront(t *Task) error {
	if d.len == len(d.tasks) {
		return errFull
	}
	d.tasks[d.head] = t
	d.len += 1
	d.head = (d.head + 1) % len(d.tasks)
	return nil
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Task

func (pq PriorityQueue) Len() int { return len(pq) }

// if true pq[i] come first
func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].rep > pq[j].rep
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x any) {
	t := x.(*Task)
	*pq = append(*pq, t)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	t := old[n-1]
	*pq = old[0 : n-1]
	return t
}

func leastInterval(tasks []byte, n int) int {
	now := 0
	execSequence := make([]string, 0, len(tasks))
	tm := make(map[byte]int)
	for _, t := range tasks {
		tm[t] += 1
	}
	// monotonic FIFO queue for waiting task
	// Priority queue to execute tasks that have more reps first
	fifo := newDeque(len(tm))
	pq := make(PriorityQueue, 0, len(tm))
	for key, value := range tm {
		fmt.Printf("Key: %s, Value: %d\n", string(key), value)
		pq.Push(&Task{
			val:          key,
			rep:          value,
			lastExecuted: -n,
		})
	}
	heap.Init(&pq)

	for {
		now += 1
		// Check the fifo queue
		for {
			t, e := fifo.peekBack()
			if e != nil {
				break
			}
			if now-t.lastExecuted > n {
				fifo.popBack()
				heap.Push(&pq, t)
			} else {
				break
			}
		}
		// Pull from the priority queue for execution
		if pq.Len() == 0 && fifo.len == 0 {
			break
		}
		if pq.Len() == 0 {
			execSequence = append(execSequence, "nil")
			continue
		}
		t := heap.Pop(&pq).(*Task)
		execSequence = append(execSequence, string(t.val))
		t.lastExecuted = now
		t.rep -= 1
		if t.rep > 0 {
			fifo.pushFront(t)
		}
	}
	fmt.Println(execSequence)
	fmt.Println("---------------")
	return now - 1
}
