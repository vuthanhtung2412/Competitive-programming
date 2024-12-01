package main

import (
	"testing"
)

func Test58(t *testing.T) {
	lengthOfLastWord("Today is a nice day")
  lengthOfLastWord("   fly me   to   the moon  ")
}

func lengthOfLastWord(s string) int {
	res := 1
	start := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] != ' ' {
			start = i
			break
		}
	}
	res = start
	for res >= 0 {
		if s[res] == ' ' {
      return start - res 
		}
		res--
	}
	return start + 1
}
