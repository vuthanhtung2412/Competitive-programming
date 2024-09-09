package list

import "fmt"

type ListNode[T any] struct {
	Val  T
	Next *ListNode[T]
}

func BuildList[T any](items []T) *ListNode[T] {
	h := &ListNode[T]{}
	res := h
	for _, v := range items {
		h.Next = &ListNode[T]{
			Val: v,
		}
		h = h.Next
	}
	return res.Next
}

func PrintList[T any](h *ListNode[T]) {
	res := ""
	iterator := h
	for iterator != nil {
		res = res + fmt.Sprintf("%v, ", iterator.Val)
		iterator = iterator.Next
	}
	fmt.Println(res)
}
