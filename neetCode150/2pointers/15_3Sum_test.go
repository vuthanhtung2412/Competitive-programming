package main

import (
	"sort"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test15(t *testing.T) {
	cs := []struct {
		nums     []int
		expected [][]int
	}{
		{
			nums:     []int{-1, 0, 1, 2, -1, -4},
			expected: [][]int{{-1, -1, 2}, {-1, 0, 1}},
		},
		{
			nums:     []int{0, 1, 1},
			expected: [][]int{},
		},
		{
			nums:     []int{0, 0, 0, 0, 0},
			expected: [][]int{{0, 0, 0}},
		},
	}

	for _, c := range cs {
		assert.Equal(t, c.expected, threeSum(c.nums))
	}
}

func threeSum(nums []int) [][]int {
	// fix position i and have 2 pointer left = i + 1, right = len(nums)-1
	// adjust left and right so that the sum equal to 0
	s := map[[3]int]struct{}{}
	sort.Ints(nums)

	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		j, k := i+1, len(nums)-1
		for j < k {
			tmp := nums[i] + nums[j] + nums[k]
			if tmp < 0 {
				j++
				for j <= k && nums[j] == nums[j-1] {
					j++
				}
				continue
			}

			if tmp > 0 {
				k--
				for j <= k && k < len(nums)-1 && nums[k] == nums[k+1] {
					k--
				}
				continue
			}

			if tmp == 0 {
				s[[3]int{nums[i], nums[j], nums[k]}] = struct{}{}
				j++
				for j <= k && nums[j] == nums[j-1] {
					j++
				}
			}
		}
	}

	res := make([][]int, 0, len(s))
	for k := range s {
		res = append(res, k[:])
	}
	return res
}
