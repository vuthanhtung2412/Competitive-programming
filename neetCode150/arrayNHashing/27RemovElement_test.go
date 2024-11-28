package main

func removeElement(nums []int, val int) int {
	end := len(nums)
	p := 0
	for p < end {
		if nums[p] == val {
			nums[p], nums[end-1] = nums[end-1], nums[p]
			end--
			continue
		}
    p++
	}
	return end
}
