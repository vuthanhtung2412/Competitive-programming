package main

import (
	"sort"
	"testing"

	"github.com/stretchr/testify/assert"
)

// https://leetcode.com/problems/merge-intervals/description/
func Test56(t *testing.T) {
	tests := []struct {
		input    [][]int
		expected [][]int
	}{
		{
			input:    [][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}},
			expected: [][]int{{1, 6}, {8, 10}, {15, 18}},
		},
		{
			input:    [][]int{{1, 4}, {4, 5}},
			expected: [][]int{{1, 5}},
		},
	}

	for _, test := range tests {
		output := merge(test.input)
		assert.Equal(t, test.expected, output, "For input %v", test.input)
	}
}

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	res := make([][]int, 0, len(intervals))
	res = append(res, intervals[0])
	for _, interval := range intervals {
		if interval[0] <= res[len(res)-1][1] && res[len(res)-1][0] <= interval[1] {
			res[len(res)-1][0] = min(res[len(res)-1][0], interval[0])
			res[len(res)-1][1] = max(res[len(res)-1][1], interval[1])
			continue
		}
		res = append(res, interval)
	}
	return res
}
