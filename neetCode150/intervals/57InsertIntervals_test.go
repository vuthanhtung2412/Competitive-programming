package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test57(t *testing.T) {
	tcs := []struct { // test cases
		intervals   [][]int
		newInterval []int
		expected    [][]int
	}{
		{
			intervals:   [][]int{{1, 3}, {6, 9}},
			newInterval: []int{2, 5},
			expected:    [][]int{{1, 5}, {6, 9}},
		},
		{
			intervals:   [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}},
			newInterval: []int{4, 8},
			expected:    [][]int{{1, 2}, {3, 10}, {12, 16}},
		},
		{
			intervals:   [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}},
			newInterval: []int{4, 8},
			expected:    [][]int{{1, 2}, {3, 10}, {12, 16}},
		},
		{
			intervals:   [][]int{{1, 5}},
			newInterval: []int{2, 3},
			expected:    [][]int{{1, 5}},
		},
	}

	for i, tc := range tcs {
		t.Run(fmt.Sprint(i), func(t *testing.T) {
			assert.Equal(t, tc.expected, insert(tc.intervals, tc.newInterval))
		})
	}
}

// intervals is sorted by start time
func insert(intervals [][]int, newInterval []int) [][]int {
	res := make([][]int, 0, len(intervals))
	var i int
	for i < len(intervals) && intervals[i][1] < newInterval[0] {
		res = append(res, intervals[i])
		i++
	}

	for i < len(intervals) {
		if intervals[i][0] <= newInterval[1] && newInterval[0] <= intervals[i][1] {
			newInterval[0] = min(newInterval[0], intervals[i][0])
			newInterval[1] = max(newInterval[1], intervals[i][1])
			i++
		} else {
			break
		}
	}
	res = append(res, newInterval)

	res = append(res, intervals[i:]...)

	return res
}
