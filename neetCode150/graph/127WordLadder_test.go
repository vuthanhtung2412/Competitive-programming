package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test127(t *testing.T) {
	cases := []struct {
		beginWord string
		endWord   string
		wordList  []string
		expected  int
	}{
		{
			beginWord: "hit",
			endWord:   "cog",
			wordList:  []string{"hot", "dot", "dog", "lot", "log", "cog"},
			expected:  5,
		},
		{
			beginWord: "hit",
			endWord:   "cog",
			wordList:  []string{"hot", "dot", "dog", "lot", "log"},
			expected:  0,
		},
	}

	for _, c := range cases {
		assert.Equal(t, c.expected, ladderLength(c.beginWord, c.endWord, c.wordList))
	}

}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordList = append(wordList, beginWord)
	l := len(wordList)

	dist := make([]int, l) // dist != 0 mean the node is visited
	dist[l-1] = 1
	q := newDeque(l)
	q.pushBack(l - 1)

	for {
		i, err := q.popFront()
		if err != nil {
			break
		}

		for j := range wordList {
			if dist[j] != 0 || !adjacent(wordList[i], wordList[j]) {
				continue
			}
			if endWord == wordList[j] {
				return dist[i] + 1
			}
			// process and queue to explore node neighbor
			dist[j] = dist[i] + 1
			q.pushBack(j)
		}
	}

	return 0
}

func adjacent(s1, s2 string) bool { // return true if words differ by a single letter
	res := false
	r1 := []rune(s1)
	r2 := []rune(s2)
	for i := range r1 {
		if r1[i] != r2[i] {
			if res {
				return false
			}
			res = true
		}
	}
	return res
}
