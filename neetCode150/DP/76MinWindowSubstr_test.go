package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test76(t *testing.T) {
	cs := []struct{ s, t, expected string }{
		{
			s:        "ADOBECODEBANC",
			t:        "ABC",
			expected: "BANC",
		},
		{
			s:        "a",
			t:        "a",
			expected: "a",
		},
		{
			s:        "a",
			t:        "aa",
			expected: "",
		},
	}
	for _, c := range cs {
		assert.Equal(t, c.expected, minWindow(c.s, c.t))
	}
}

func minWindow(s string, t string) string {
	sr := []rune(s) // sources array of rune
	tr := []rune(t) // target array of rune
	if len(tr) > len(sr) {
		return ""
	}
	lack := map[rune]int{}
	extra := map[rune]int{}

	for _, r := range tr {
		_, ok := lack[r]
		if !ok {
			lack[r] = 0
		}
		lack[r]++
	}

	l := 0
	resl, resr := 0, len(sr)+1
	for r := 0; r < len(sr); r++ {
		// if substring lack char
		_, ok := lack[sr[r]]
		if !ok {
			if _, ok := extra[sr[r]]; !ok {
				extra[sr[r]] = 0
			}
			extra[sr[r]]++
		} else {
			lack[sr[r]]--
			if lack[sr[r]] == 0 {
				delete(lack, sr[r])
			}
		}

		for len(lack) == 0 {
			if r-l < resr-resl {
				resl, resr = l, r
			}

			// if there is extra
			c := extra[sr[l]]
			if c > 0 {
				extra[sr[l]]--
			} else {
				lack[sr[l]] = 1
			}

			l++
		}
	}

	if resr > len(sr) {
		return ""
	}
	return string(sr[resl : resr+1])
}
