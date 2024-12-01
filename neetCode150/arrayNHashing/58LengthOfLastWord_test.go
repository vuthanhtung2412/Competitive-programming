package main

import (
	"strings"
	"testing"
)


func Test58(t *testing.T) {
  lengthOfLastWord("Today is a nice day")
}
func lengthOfLastWord(s string) int {
  curr := 0
  s = strings.TrimSpace(s)
  for _, r := range s{
    if r == ' ' {
      curr = 0
      continue
    }
    curr ++
  }
  return curr
}
