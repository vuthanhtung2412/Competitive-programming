package main

import "fmt"

// Intuition
// We need to assign increasing candies (by 1) for increasing ratings (equality excluded) subarray either from the left or from the right
// When ever the increasing subarray stop assign

func candy(ratings []int) int {
	l := make([]int, len(ratings))
	for i := range ratings {
		if i == 0 {
			l[i] = 1
      continue
		}
		if ratings[i] > ratings[i-1] {
			l[i] = l[i-1] + 1
			continue
		}
		l[i] = 1
	}
	r := make([]int, len(ratings))
	r[len(ratings)-1] = 1
	for i := len(ratings) - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			r[i] = r[i+1] + 1
			continue
		}
		r[i] = 1
	}

  fmt.Println(l)
  fmt.Println(r)
  res := 0
  for i := 0; i < len(ratings); i++ {
    res += max(l[i], r[i])
  }
  return res
}
