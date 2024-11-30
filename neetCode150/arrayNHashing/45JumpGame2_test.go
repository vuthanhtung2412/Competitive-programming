package main 

// minJ[i] = min(minJ[j] for j in range i if j + nums[j] > n)
func jump (nums []int) int {
  if len(nums) == 1{
    return 0
  }
  currStep := 0
  nextLast := 0
  currLast := 0
  for i, s := range nums {
    nextLast = max(nextLast, i+s)
    if (nextLast >= len(nums)-1){
      return currStep + 1 
    }
    if i >= currLast {
      if currLast == nextLast{
        break
      }
      currLast = nextLast
      currStep ++
    }
  }
  return -1
}
