package main

func removeDuplicates(nums []int) int {
  count := 1
  for i := 1; i < len(nums); i++{
    if nums[i] == nums[i-1] {
      continue
    }
    nums[count] = nums[i]
    count++
  }
  return count
}
