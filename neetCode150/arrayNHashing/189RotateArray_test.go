package main

func rotate(nums []int, k int) {
	for i := 0; i < len(nums)/2; i++ {
		nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
	}
	k = k % len(nums)
	for i := 0; i < k/2; i++ {
		nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
	}
	for i := k; i < (len(nums)+k)/2; i++ {
		nums[i], nums[len(nums)-1-i+k] = nums[len(nums)-1-i+k], nums[i]
	}
}
