package main

func helper(s1, s2 string) string {
  var i int
  for i = 0; i < min(len(s1), len(s2)); i++ {
    if s1[i] != s2[i]{
      break
    }
  }
  if len(s1) <= len(s2){
    return s1[:i]
  }
  return s2[:i]
}

func longestCommonPrefix(strs []string) string {
  res := strs[0]  
  for i:= 1; i < len(strs); i++ {
    res = helper(strs[i], res)
    if res == ""{
      break
    }
  }
  return res
}

