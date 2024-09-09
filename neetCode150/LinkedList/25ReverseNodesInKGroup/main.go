package main

import (
	. "competitiveProgramming/neetCode150/LinkedList"
)

func main() {
	PrintList(reverseKGroup(BuildList[int]([]int{1, 2, 3, 4, 5}), 2))
	PrintList(reverseKGroup(BuildList[int]([]int{1, 2, 3, 4, 5}), 3))
	PrintList(reverseKGroup(BuildList[int]([]int{1, 2, 3, 4, 5}), 5))
	PrintList(reverseKGroup(BuildList[int]([]int{1, 2, 3, 4, 5}), 6))
	PrintList(reverseKGroup(BuildList[int]([]int{1, 2, 3, 4}), 2))

}

func reverse(head *ListNode[int], k int) (h, t, next *ListNode[int], b bool) {
	var n1, n2 *ListNode[int]
	// Check size
	n1 = head
	for i := 0; i < k; i++ {
		if n1 == nil {
			return nil, head, nil, false
		}
		n1 = n1.Next
	}
	// Reverse
	n1 = nil
	n2 = head
	for i := 0; i < k; i++ {
		temp := n2.Next
		n2.Next = n1
		n1 = n2
		n2 = temp
	}
	return head, n1, n2, true
}

func reverseKGroup(head *ListNode[int], k int) *ListNode[int] {
	prev, res, next, b := reverse(head, k)
	if !b {
		return res
	}
	for {
		h, t, n, b := reverse(next, k)
		prev.Next = t
		if !b {
			break
		}
		prev = h
		next = n
	}
	return res
}
