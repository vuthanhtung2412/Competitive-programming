package main

import (
	"fmt"
	"testing"
)

func Test5(t *testing.T) {
	fmt.Println(longestPalindrome("bb"))
	fmt.Println(longestPalindrome("bbb"))
}
func longestPalindrome(s string) string {
	// Intuition
	// Check mid point for even / uneven centered separately

	if len(s) == 1 {
		return s
	}

	l, r := 0, 1

	// uneven center
	for i := range s {
		// find max palindrome center at s[i]
		for j := 1; j <= min(i, len(s)-i-1); j++ {
			if s[i-j] != s[i+j] {
				if 2*j-1 > r-l {
					l = i - j + 1
					r = i + j
				}
				break
			}
			// Edge case : end of the string, we won't encounter unidentical chars
			if j == min(i, len(s)-i-1) {
				if 2*j+1 > r-l {
					l = i - j
					r = i + j + 1
				}
			}
		}
	}

	// even center
	for i := 0; i < len(s)-1; i++ {
		for j := 1; j <= min(i+1, len(s)-i-1); j++ {
			if s[i-j+1] != s[i+j] {
				if 2*j-2 > r-l {
					l = i - j + 2
					r = i + j
				}
				break
			}
			// Edge case : end of the string, we won't encounter unidentical chars
			if j == min(i+1, len(s)-i-1) {
				if 2*j > r-l {
					l = i - j + 1
					r = i + j + 1
				}
			}
		}
	}

	return s[l:r]
}
