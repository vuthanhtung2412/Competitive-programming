package main 

func merge(nums1 []int, m int, nums2 []int, n int) {
  res := make([]int, m+n)    
  p1, p2 := 0,0
  for p1 < m && p2 < n{
    if nums1[p1] <= nums2[p2] {
      res[p1+p2] = nums1[p1]
      p1++
      continue
    } 
    res[p1+p2] = nums2[p2]
    p2++
  }
  if p1 == m{
    for p2 < n{
      res[p1+p2] = nums2[p2]
      p2++
    }
  } else {
    for p1 < m{
      res[p1+p2] = nums1[p1]
      p1++
    }
  }
  copy(nums1, res)
}
