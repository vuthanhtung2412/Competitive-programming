package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test122(t *testing.T) {
	tests := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{2, 1, 2, 1, 0, 1, 2},
			expected: 3,
		}, {
			input:    []int{4, 1, 2, 7},
			expected: 6,
		},
	}
	for _, test := range tests {
		output := maxProfit(test.input)
		assert.Equal(t, test.expected, output, "For input %v", test.input)
	}
}

func maxProfit(prices []int) int {
	next := make([]int, len(prices))
	stack := make([]int, 0, len(prices))
	for i, p := range prices {
		for len(stack) > 0 {
			if prices[last(stack)] < p {
				next[last(stack)] = i
				stack = stack[:len(stack)-1]
				continue
			}
			break
		}
		stack = append(stack, i)
	}
	res := 0
	curr := 0
	for i := 1; i < len(prices); i++ {
    if curr == -1 {
      if next[i] > 0 {
        curr = i
      }
      continue
    }
		if i < next[curr] {
			if prices[i] < prices[curr] {
				curr = i
			}
			continue
		}
		res += prices[next[curr]] - prices[curr]
		if next[i] > 0 {
			curr = i
		} else {
      curr = -1
    }
	}
	return res
}

func last(s []int) int {
	return s[len(s)-1]
}
