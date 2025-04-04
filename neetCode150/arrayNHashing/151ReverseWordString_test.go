package main

import (
	"fmt"
	"strings"
	"testing"
)

func Test151(t *testing.T) {
	reverseWords("  hello world  ")
  reverseWords("   a good   example  ")
}

func reversePart(runes []rune, s, e int) {
	for i := s; i <= (s+e)/2; i++ {
		runes[i], runes[e+s-i] = runes[e+s-i], runes[i]
	}
}

func removeSpaces(runes []rune) []rune {
	// trim intermediate extra spaces
	wid := 0
	for i, r := range runes {
		if r != ' ' {
			if i > 0 && runes[i-1] == ' ' {
				runes[wid] = ' '
				wid++
			}
			runes[wid] = r
			wid++
		}
	}
	runes = runes[:wid]
  if runes[0] == ' ' {
    runes = runes[1:]
  }
  return runes
}

func reverseWords(s string) string {
	runes := []rune(strings.TrimSpace(s))
  runes = removeSpaces(runes)
	fmt.Println(string(runes))
	for i := 0; i < len(runes)/2; i++ {
		runes[i], runes[len(runes)-1-i] = runes[len(runes)-1-i], runes[i]
	}
	b := 0
	for i, r := range runes {
		if r == ' ' {
			reversePart(runes, b, i-1)
			b = i + 1
		}
	}
	reversePart(runes, b, len(runes)-1)
	return string(runes)
}
