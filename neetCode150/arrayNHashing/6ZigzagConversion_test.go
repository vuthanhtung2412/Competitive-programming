package main

import (
	"testing"
)

func Test6(t *testing.T){
  // var rs []rune
  // rs = append(rs, 'a')
  // fmt.Println(string(rs))
}
func convert(s string, numRows int) string {
  if numRows ==1 {
    return s
  }
  rss := make([][]rune, numRows)    
  l := 0
  increase := true
  for _, r := range s{
    rss[l] = append(rss[l], r)
    if increase {
      l++
      if l == numRows-1{
        increase = false
      }
      continue
    }
    l--
    if l == 0{
      increase = true 
    }
  }
  res := []rune{}
  for _, rs := range rss{
    res = append(res, rs...)
  }
  return string(res)
}
