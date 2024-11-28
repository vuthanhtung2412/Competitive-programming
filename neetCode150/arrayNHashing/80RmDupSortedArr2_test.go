package main 

func removeDuplicates2(nums []int) int {
  dup := false
  count := 1
  for i := 1; i < len(nums); i++{
    if nums[i] == nums[i-1]{
      if dup{
        continue
      }
      nums[count] = nums[i]
      dup = true
      count++
      continue
    }
    nums[count] = nums[i]
    dup = false
    count ++
  }
  return count
}
