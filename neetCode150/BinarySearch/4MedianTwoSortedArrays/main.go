package main

import "fmt"

func main() {
	fmt.Println(findMedianSortedArrays([]int{1, 3}, []int{2}))
	fmt.Println(findMedianSortedArrays([]int{1, 2, 5, 5, 8}, []int{3, 4, 6, 9, 10}))
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	mergedArray := make([]int, 0, len(nums1)+len(nums2))
	h1, h2 := 0, 0
	for h1 < len(nums1) && h2 < len(nums2) {
		if nums1[h1] <= nums2[h2] {
			mergedArray = append(mergedArray, nums1[h1])
			h1++
		} else {
			mergedArray = append(mergedArray, nums2[h2])
			h2++
		}
	}
	if h1 == len(nums1) {
		mergedArray = append(mergedArray, nums2[h2:]...)
	} else {
		mergedArray = append(mergedArray, nums1[h1:]...)
	}
	fmt.Println(mergedArray)
	if len(mergedArray)%2 == 1 {
		return float64(mergedArray[len(mergedArray)/2])
	}
	return float64(mergedArray[len(mergedArray)/2]+mergedArray[len(mergedArray)/2-1]) / 2
}
