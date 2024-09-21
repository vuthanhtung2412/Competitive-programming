package main

import (
	"fmt"
	"slices"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test131(t *testing.T) {
	cs := []struct {
		s        string
		expected [][]string
	}{
		{
			s:        "aab",
			expected: [][]string{{"a", "a", "b"}, {"aa", "b"}},
		},
		{
			s:        "aaba",
			expected: [][]string{{"a", "a", "b", "a"}, {"a", "aba"}, {"aa", "b", "a"}},
		},
	}

	for i, c := range cs {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			assert.Equal(t, c.expected, partition(c.s))
		})
	}
}

func partition(s string) [][]string {
	bs := []byte(s)
	res := [][]string{}

	curr := make([]string, 0, len(bs))

	var rec func(start int)
	rec = func(start int) {
		for i := start + 1; i <= len(bs); i++ {
			if !isPalindrome(bs[start:i]) {
				continue
			}
			curr = append(curr, string(bs[start:i]))
			if i == len(bs) {
				res = append(res, slices.Clone(curr))
				curr = curr[:len(curr)-1]
				continue
			}
			rec(i)
			curr = curr[:len(curr)-1]
		}
	}

	rec(0)
	return res
}

func isPalindrome(s []byte) bool {
	l, r := 0, len(s)-1
	for l < r {
		if s[l] != s[r] {
			return false
		}
		l++
		r--
	}
	return true
}
