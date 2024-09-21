package main

import (
	"sort"
	"strconv"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test435(t *testing.T) {
	cs := []struct {
		intervals [][]int
		expected  int
	}{
		{
			intervals: [][]int{{1, 2}, {2, 3}, {3, 4}, {1, 3}},
			expected:  1,
		},
		{
			intervals: [][]int{{1, 2}, {1, 2}, {1, 2}},
			expected:  2,
		},
		{
			intervals: [][]int{{1, 2}, {2, 3}},
			expected:  0,
		},
	}

	for i, c := range cs {
		t.Run(strconv.Itoa(i), func(t *testing.T) {
			assert.Equal(t, c.expected, eraseOverlapIntervals(c.intervals))
		})
	}
}
func eraseOverlapIntervals(intervals [][]int) int {
	// if overlap still exists, there are interval to be removed
	// In ascending start time order, overlap condition is end[prev] > start[later]
	// If overlap. keep max(ending time from prev interval) as low as possible

	// Implementation
	// if the intervals are sorted in start time increasing order
	// if the curr interval overlaps with max(end time from prev interval)
	// remove the the interval with later end time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	count := 0
	maxEnd := int(-5 * 1e4)
	for _, i := range intervals {
		if maxEnd > i[0] {
			count++
			maxEnd = min(maxEnd, i[1])
			continue
		}
		maxEnd = max(maxEnd, i[1])
	}
	return count
}
