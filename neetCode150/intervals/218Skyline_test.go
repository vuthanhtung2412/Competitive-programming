package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test218(t *testing.T) {
	// fmt.Println(mergeSkyline([][2]int{{2, 10}, {9, 0}}, [][2]int{{3, 15}, {7, 0}}))
	// fmt.Println(mergeSkyline([][2]int{{0, 3}, {2, 0}}, [][2]int{{3, 15}, {7, 0}}))
	// fmt.Println(getSkyline([][3]int{{2, 9, 10}, {3, 7, 15}, {5, 12, 12}}))
	// fmt.Println("---")
	tests := []struct {
		input    [][3]int
		expected [][2]int
	}{
		{
			input:    [][3]int{{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}},
			expected: [][2]int{{2, 10}, {3, 15}, {7, 12}, {12, 0}, {15, 10}, {20, 8}, {24, 0}},
		}, {
			input:    [][3]int{{0, 2, 3}, {2, 5, 3}},
			expected: [][2]int{{0, 3}, {5, 0}},
		},
	}
	for _, test := range tests {
		output := getSkyline(test.input)
		assert.Equal(t, test.expected, output, "For input %v", test.input)
	}
}

func getSkyline(buildings [][3]int) [][2]int {
	if len(buildings) == 1 {
		return [][2]int{{buildings[0][0], buildings[0][2]}, {buildings[0][1], 0}}
	}
	if len(buildings) == 2 {
		return mergeSkyline(
			[][2]int{{buildings[0][0], buildings[0][2]}, {buildings[0][1], 0}},
			[][2]int{{buildings[1][0], buildings[1][2]}, {buildings[1][1], 0}},
		)
	}
	return mergeSkyline(
		getSkyline(buildings[:len(buildings)/2]),
		getSkyline(buildings[len(buildings)/2:]),
	)
}

func mergeSkyline(s1, s2 [][2]int) [][2]int {
	res := make([][2]int, 0, len(s1)+len(s2))
	p1, p2 := 0, 0
	h1, h2 := 0, 0
	for p1 < len(s1) && p2 < len(s2) {
		if s1[p1][0] == s2[p2][0] {
			if max(h1, h2) != max(s1[p1][1], s2[p2][1]) {
				res = append(res, [2]int{s1[p1][0], max(s1[p1][1], s2[p2][1])})
			}
			h1 = s1[p1][1]
			h2 = s2[p2][1]
			p1++
			p2++
		} else if s1[p1][0] < s2[p2][0] {
			if max(h1, h2) != max(s1[p1][1], h2) {
				res = append(res, [2]int{s1[p1][0], max(h2, s1[p1][1])})
			}
			h1 = s1[p1][1]
			p1++
		} else {
			if max(h1, h2) != max(s2[p2][1], h1) {
				res = append(res, [2]int{s2[p2][0], max(h1, s2[p2][1])})
			}
			h2 = s2[p2][1]
			p2++
		}
	}
	if p1 == len(s1) {
		res = append(res, s2[p2:]...)
	} else {
		res = append(res, s1[p1:]...)
	}
	return res
}
