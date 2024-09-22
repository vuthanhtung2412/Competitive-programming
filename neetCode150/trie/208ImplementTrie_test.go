package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test208(t *testing.T) {
	cs := []struct {
		c        []string
		args     [][]any
		expected []any
	}{
		{
			c:        []string{"insert", "search", "search", "startsWith", "insert", "search"},
			args:     [][]any{{"apple"}, {"apple"}, {"app"}, {"app"}, {"app"}, {"app"}},
			expected: []any{nil, true, false, true, nil, true},
		},
	}

	for i, c := range cs {
		t.Run(fmt.Sprintf("%d", i), func(t *testing.T) {
			tr := Constructor() // Assuming Constructor initializes a Trie instance
			for j := range c.c {
				res := execute(&tr, c.c[j], c.args[j]...)
				assert.Equal(t, c.expected[j], res)
			}
		})
	}
}

func execute(t *Trie, c string, args ...any) any {
	switch c {
	case "insert":
		t.Insert(args[0].(string))
		return nil
	case "search":
		return t.Search(args[0].(string))
	case "startsWith":
		return t.StartsWith(args[0].(string))
	}
	panic("command not found")
}

// Slice of byte pass by reference solution

// This Trie on only work for alphabetic char
type Trie struct {
	edges map[byte]*Trie
	isEnd bool
}

func Constructor() Trie {
	return Trie{
		edges: map[byte]*Trie{},
		isEnd: false,
	}
}

func (t *Trie) Insert(word string) {
	if len(word) == 0 {
		t.isEnd = true
		return
	}
	if _, ok := t.edges[word[0]]; !ok {
		newTrie := Constructor()
		t.edges[word[0]] = &newTrie
	}
	t.edges[word[0]].Insert(word[1:])
}

func (t *Trie) Search(word string) bool {
	if len(word) == 0 {
		return t.isEnd
	}
	if tr, ok := t.edges[word[0]]; ok {
		return tr.Search(word[1:])
	}
	return false
}

func (t *Trie) StartsWith(prefix string) bool {
	if len(prefix) == 0 {
		return true
	}
	if tr, ok := t.edges[prefix[0]]; ok {
		return tr.StartsWith(prefix[1:])
	}
	return false
}
