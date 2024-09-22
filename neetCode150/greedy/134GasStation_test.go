package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test134(t *testing.T) {
	tests := []struct {
		gas      []int
		cost     []int
		expected int
	}{
		{
			gas:      []int{1, 2, 3, 4, 5},
			cost:     []int{3, 4, 5, 1, 2},
			expected: 3,
		},
		{
			gas:      []int{2, 3, 4},
			cost:     []int{3, 4, 3},
			expected: -1,
		},
	}

	for _, test := range tests {
		output := canCompleteCircuit(test.gas, test.cost)
		assert.Equal(t, test.expected, output)
	}
}

func canCompleteCircuit(gas []int, cost []int) int {
	// The point we want to accumulate the largest amount of gax before spending it
	// Largest sum subarray but in the case that 2 end of the array connected
	// One trick is to iterate the array twice
	remain := make([]int, 2*len(gas))
	can := 0
	for i := range remain {
		remain[i] = gas[i%len(gas)] - cost[i%len(cost)]
		can += remain[i]
	}

	// if the amount of gas available is lower that the total cost
	if can < 0 {
		return -1
	}

	prefixSum := 0
	max := int(-1e4 - 1)
	s := 0
	var res int
	for e := range remain {
		if prefixSum < 0 {
			s = e
			prefixSum = 0
		}
		prefixSum += remain[e]
		if prefixSum > max {
			res = s % len(gas)
		}
	}

	return res
}
