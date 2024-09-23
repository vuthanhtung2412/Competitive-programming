package main

import (
	"testing"
)

func Test5(t *testing.T) {}

func longestPalindrome(s string) string {
	// Intuition
	// This has some similarity with Maximum Sum Array problem
	// First need to solve the problem of palindrome(s, i) returns the length of the longest palindrome that ends with index i (inclusive)
	// palindrome(s,i) =
	// 		if s[i-1-palindrome(s,i-1)-1] == s[i] : palindrome(s,i)
	// 		else : 1
	// longestPalindrome(s) = s[maxIndex(palindrome(s,i)) - palindrome(s,i) : maxIndex(palindrome(s,i))]
	res := ""
	// TODO
	return res
}
