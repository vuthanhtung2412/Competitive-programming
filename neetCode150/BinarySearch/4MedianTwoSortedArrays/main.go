package main

import "fmt"

func main() {
	fmt.Println(findMedianSortedArrays3([]int{1, 3}, []int{2}))
	fmt.Println(findMedianSortedArrays3([]int{1, 2, 5, 5, 8}, []int{3, 4, 6, 9, 10}))
	fmt.Println(findMedianSortedArrays3([]int{1, 2}, []int{3, 4}))
	fmt.Println(findMedianSortedArrays3([]int{3}, []int{-2, -1}))
	fmt.Println(findMedianSortedArrays3([]int{1}, []int{1}))
	fmt.Println(findMedianSortedArrays3([]int{}, []int{1, 2}))
	fmt.Println(findMedianSortedArrays3([]int{1}, []int{2, 3}))
	fmt.Println(findMedianSortedArrays3([]int{1, 2, 3, 4, 5, 6}, []int{1}))
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

// TODO : Binary search approach
// Insights smaller (left) half and greater (right) half
// Partition 2 array each into a left subarray and right subarray : l1, r1, l2, r2
// Constraints
// len(l1) + len(l2) = len(r1) + len(r2) (+1) => len(l1) + len(l2) = len(nums1) + len(nums2)
// l1[-1] < r1[0] & r2[0] ; l2[-1] < r1[0] & r2[0]
// Edge case :
// + len(l1) >= half
// + len(l1) = 0
// + len(l1) + len(nums2) < half
// In context of this many edge cases it might worth try adding a lower to the beginning of the array and upper limit the end
func findMedianSortedArrays1(nums1 []int, nums2 []int) float64 {
	l, r := 0, len(nums1) // lower and upper bound of number of element in l1 partition
	half := (len(nums1) + len(nums2)) / 2
	isEven := (len(nums1)+len(nums2))%2 == 0
	nums1 = append(append([]int{-1e6 - 1}, nums1...), 1e6+1) // O(n)
	nums2 = append(append([]int{-1e6 - 1}, nums2...), 1e6+1) // O(n)
	var m int
	for l <= r {
		m = (l + r) / 2
		if m > half {
			r = m
			continue
		}
		if half-m > len(nums2)-2 {
			l = m + 1
			continue
		}
		if nums1[m] >= nums2[half-m+1] {
			r = m
			continue
		}
		if nums1[m] <= nums2[half-m+1] && nums1[m+1] >= nums2[half-m] {
			break
		}
		l = m + 1
	}
	fmt.Printf("mid point : %d\n", m)
	if isEven {
		return float64(max(nums1[m], nums2[half-m])+min(nums1[m+1], nums2[half-m+1])) / 2
	}
	return float64(min(nums1[m+1], nums2[half-m+1]))
}

// 2 pointer
func findMedianSortedArrays2(nums1 []int, nums2 []int) float64 {
	isEven := (len(nums1)+len(nums2))%2 == 0
	if len(nums2) == 0 {
		if isEven {
			return float64(nums1[len(nums1)/2]+nums1[len(nums1)/2-1]) / 2
		}
		return float64(nums1[len(nums1)/2])
	}
	if len(nums1) == 0 {
		if isEven {
			return float64(nums2[len(nums2)/2]+nums2[len(nums2)/2-1]) / 2
		}
		return float64(nums2[len(nums2)/2])
	}
	half := (len(nums1) + len(nums2)) / 2
	h1, h2 := 0, 0
	for h1 < len(nums1) && h2 < len(nums2) {
		if nums1[h1] <= nums2[h2] {
			h1++
		} else {
			h2++
		}
		if h1+h2 == half {
			break
		}
	}
	if h1 == len(nums1) {
		h2 = half - h1
	} else if h2 == len(nums2) {
		h1 = half - h2
	}

	if h1 == 0 && h2 == len(nums2) {
		if isEven {
			return float64(nums2[len(nums2)-1]+nums1[0]) / 2
		}
		return float64(max(nums2[len(nums2)-1], nums1[0]))
	}
	if h2 == 0 && h1 == len(nums1) {
		if isEven {
			return float64(nums1[len(nums1)-1]+nums2[0]) / 2
		}
		return float64(max(nums1[len(nums1)-1], nums2[0]))
	}
	if h1 == 0 {
		if isEven {
			return float64(min(nums1[0], nums2[h2])+nums2[h2-1]) / 2
		}
		return float64(min(nums1[0], nums2[h2]))
	}
	if h2 == 0 {
		if isEven {
			return float64(min(nums2[0], nums1[h1])+nums1[h1-1]) / 2
		}
		return float64(min(nums2[0], nums1[h1]))
	}
	if h1 == len(nums1) {
		if isEven {
			return float64(max(nums1[len(nums1)-1], nums2[h2-1])+nums2[h2]) / 2
		}
		return float64(nums2[h2])
	}
	if h2 == len(nums2) {
		if isEven {
			return float64(max(nums2[len(nums2)-1], nums1[h1-1])+nums1[h1]) / 2
		}
		return float64(nums1[h1])
	}
	if isEven {
		return float64(max(nums2[h2-1], nums1[h1-1])+min(nums2[h2], nums1[h1])) / 2
	}
	return float64(min(nums1[h1], nums2[h2]))
}

const (
	s int = -1e6 - 1 // smallest
	b int = 1e6 + 1  // biggest
)

func cmpPartition(l1, l2, r1, r2 []int, even bool) (int, float64) {
	var s1, s2, b1, b2 int
	if len(l1) == 0 {
		s1 = s
	} else {
		s1 = l1[len(l1)-1]
	}

	if len(l2) == 0 {
		s2 = s
	} else {
		s2 = l2[len(l2)-1]
	}

	if len(r1) == 0 {
		b1 = b
	} else {
		b1 = r1[0]
	}

	if len(r2) == 0 {
		b2 = b
	} else {
		b2 = r2[0]
	}

	if s1 > b2 {
		return -1, 0 // Search left
	}
	if s1 <= b2 && s2 <= b1 {
		if even {
			return 0, float64(max(s1, s2)+min(b1, b2)) / 2
		}
		return 0, float64(min(b1, b2))
	}
	return 1, 0 // search right
}

func findMedianSortedArrays3(nums1 []int, nums2 []int) float64 {
	l, r := 0, len(nums1) // lower and upper bound of number of element in l1 partition
	half := (len(nums1) + len(nums2)) / 2
	even := (len(nums1)+len(nums2))%2 == 0
	var m int // l <= m <= r
	var s1, s2, b1, b2 int
	for l <= r {
		m = (l + r) / 2
		fmt.Printf("l : %d, r : %d, m : %d\n", l, r, m)
		if m > half {
			r = m
			continue
		}
		if half-m > len(nums2) {
			l = m + 1
			continue
		}

		if m == 0 {
			s1 = s
		} else {
			s1 = nums1[m-1]
		}

		if m == half {
			s2 = s
		} else {
			s2 = nums2[half-m-1]
		}

		if m == len(nums1) {
			b1 = b
		} else {
			b1 = nums1[m]
		}

		if half-m == len(nums2) {
			b2 = b
		} else {
			b2 = nums2[half-m]
		}

		if s1 <= b2 && s2 <= b1 {
			if even {
				return float64(max(s1, s2)+min(b1, b2)) / 2
			}
			return float64(min(b1, b2))
		}
		if s1 > b2 {
			r = m
			continue
		}
		l = m + 1
	}
	return 0
}
