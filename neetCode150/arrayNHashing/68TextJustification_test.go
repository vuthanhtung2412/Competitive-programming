package main

import "strings"

func fullJustify(words []string, maxWidth int) []string {
	res := []string{}
	currLen := 0
	startWord := 0
	for i, s := range words {
		if currLen+i-startWord+len(s) > maxWidth { // start a new line
			if i-startWord == 1 {
				res = append(res, words[startWord]+strings.Repeat(" ", maxWidth-len(words[startWord])))
			} else {
				spaces := (maxWidth - currLen) / (i - startWord - 1)
				spacesL := (maxWidth - currLen) % (i - startWord - 1)
				tmp := make([]rune, 0, maxWidth)
				for j := 0; j < i-startWord; j++ {
					if j == i-startWord-1 {
						tmp = append(tmp, []rune(words[startWord+j])...)
						continue
					}
					if j < spacesL {
						tmp = append(tmp, []rune(words[startWord+j])...)
						tmp = append(tmp, []rune(strings.Repeat(" ", spaces+1))...)
						continue
					}
					tmp = append(tmp, []rune(words[startWord+j])...)
					tmp = append(tmp, []rune(strings.Repeat(" ", spaces))...)
				}
				res = append(res, string(tmp))
			}
			// combine words from startWord to i-1
			startWord = i
			currLen = 0
		}
		currLen += len(s)
	}

	tmp := make([]rune, 0, maxWidth)
	for j := startWord; j < len(words); j++ {
		if j == len(words)-1 {
			tmp = append(tmp, []rune(words[j])...)
			tmp = append(tmp, []rune(strings.Repeat(" ", maxWidth-len(tmp)))...)
			continue
		}
		tmp = append(tmp, []rune(words[j])...)
		tmp = append(tmp, ' ')
	}
	res = append(res, string(tmp))
	return res
}

func fullJustifyString(words []string, maxWidth int) []string {
	res := []string{}
	currLen := 0
	startWord := 0
	for i, s := range words {
		if currLen+i-startWord+len(s) > maxWidth { // start a new line
			if i-startWord == 1 {
				res = append(res, words[startWord]+strings.Repeat(" ", maxWidth-len(words[startWord])))
			} else {
				spaces := (maxWidth - currLen) / (i - startWord - 1)
				spacesL := (maxWidth - currLen) % (i - startWord - 1)
				tmp := ""
				for j := 0; j < i-startWord; j++ {
					if j == i-startWord-1 {
						tmp = tmp + words[startWord+j]
						continue
					}
					if j < spacesL {
						tmp = tmp + words[startWord+j] + strings.Repeat(" ", spaces+1)
						continue
					}
					tmp = tmp + words[startWord+j] + strings.Repeat(" ", spaces)
				}
				res = append(res, tmp)
			}
			// combine words from startWord to i-1
			startWord = i
			currLen = 0
		}
		currLen += len(s)
	}

	tmp := ""
	for j := startWord; j < len(words); j++ {
		if j == len(words)-1 {
			tmp += words[j]
			tmp += strings.Repeat(" ", maxWidth-len(tmp))
			continue
		}
		tmp += words[j] + " "
	}
	res = append(res, tmp)
	return res
}
