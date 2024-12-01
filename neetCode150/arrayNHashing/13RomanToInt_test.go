package main

func romanToInt(s string) int {
	c2i := map[string]int{
		"I":  1,
		"V":  5,
		"X":  10,
		"IV": 4,
		"IX": 9,
		"L":  50,
		"C":  100,
		"XL": 40,
		"XC": 90,
		"D":  500,
		"M":  1000,
		"CD": 400,
		"CM": 900,
	}
	res := 0
	i := 0
	for i < len(s) {
		if i == len(s)-1 {
			res += c2i[string(s[i])]
			break
		}
		val, ok := c2i[s[i:i+2]]
		if ok {
			res += val
			i += 2
			continue
		}
		res += c2i[string(s[i])]
		i++
	}
	return res
}
