package main

import "math/rand/v2"


type RandomizedSet struct {
	m map[int]int
  s []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		map[int]int{},
    []int{},
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	_, ok := this.m[val]
	if ok {
		return false
	}
	this.m[val] = len(this.s)
  this.s = append(this.s, val)
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	p, ok := this.m[val]
  if !ok {
    return false
  }
  // The same pattern is also utilized in heap data structure
  this.s[p] = this.s[len(this.s)-1]
  this.m[this.s[p]] = p
  this.s = this.s[:len(this.s)-1]
  delete(this.m, val)
  return true
}

func (this *RandomizedSet) GetRandom() int {
  i := rand.IntN(len(this.s))
  return this.s[i]
}
