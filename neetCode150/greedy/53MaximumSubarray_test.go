package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test53(t *testing.T) {
	tests := []struct {
		nums     []int
		expected int
	}{
		{
			nums:     []int{-2, 1, -3, 4, -1, 2, 1, -5, 4},
			expected: 6,
		},
		{
			nums:     []int{1},
			expected: 1,
		},
		{
			nums:     []int{5, 4, -1, 7, 8},
			expected: 23,
		},
	}

	for _, test := range tests {
		output := maxSubArray(test.nums)
		assert.Equal(t, test.expected, output, "For input %v", test.nums)
	}
}

func maxSubArray(nums []int) int {
	// Intuition
	// First solve the problem the subarray that has the max sum that end at index e (inclusive)
	// maxSubArray(nums, e) = nums[e] + max(0, maxSubArray(nums, e-1))
	// maxSubArray(nums) = max([maxSubArray(nums,e) for e range(len(nums))])
	res := int(-1e4 - 1)
	prev := int(-1e4 - 1)
	for _, num := range nums {
		prev = num + max(prev, 0)
		if prev > res {
			res = prev
		}
	}

	return res
}
