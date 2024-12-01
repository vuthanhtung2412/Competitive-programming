package main

func hIndex(citations []int) int {
	a := make([]int, len(citations)+1)
	for _, c := range citations {
		if c > len(citations) {
			a[len(citations)] += 1
			continue
		}
		a[c]++
	}

  for i := len(citations); i > 0; i-- {
    if a[i] >= i {
      return i
    }
    a[i-1] += a[i]
  }
  return 0
}
