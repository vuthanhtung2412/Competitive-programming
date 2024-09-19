package main

import (
	"errors"
	"fmt"
	"testing"
)

func Test210(t *testing.T) {
	fmt.Println(findOrder1(2, [][]int{
		{1, 0},
	}))

	fmt.Println(findOrder1(2, [][]int{
		{0, 1}, {1, 0},
	}))

	fmt.Println(findOrder1(4, [][]int{
		{1, 0}, {2, 0}, {3, 1}, {3, 2},
	}))

	fmt.Println(findOrder1(1, [][]int{}))
}

var (
	errLoop = errors.New("loop dependency")
)

func findOrder(numCourses int, prerequisites [][]int) []int {
	req := make([][]int, numCourses) // map of requirements
	for _, p := range prerequisites {
		req[p[0]] = append(req[p[0]], p[1])
	}
	taken := make([]bool, numCourses)
	checkLoop := make([]bool, numCourses)
	seq := make([]int, 0, numCourses)

	// take course
	for i := 0; i < numCourses; i++ {
		s, err := takeCourse(i, req, taken, checkLoop, numCourses)
		if err != nil {
			return []int{}
		}
		seq = append(seq, s...)
	}
	return seq
}

func takeCourse(c int, req [][]int, taken []bool, checkLoop []bool, numCourse int) ([]int, error) {
	if taken[c] {
		return []int{}, nil
	}

	if checkLoop[c] {
		return []int{}, errLoop
	}

	checkLoop[c] = true

	res := make([]int, 0, numCourse)
	for _, r := range req[c] {
		ct, err := takeCourse(r, req, taken, checkLoop, numCourse)
		if err != nil {
			return []int{}, err
		}
		res = append(res, ct...)
	}
	taken[c] = true
	res = append(res, c)

	checkLoop[c] = false

	return res, nil
}

func findOrder1(numCourses int, prerequisites [][]int) []int { // inner function
	req := make([][]int, numCourses) // map of requirements
	for _, p := range prerequisites {
		req[p[0]] = append(req[p[0]], p[1])
	}
	taken := make([]bool, numCourses)
	checkLoop := make([]bool, numCourses)
	seq := make([]int, 0, numCourses)

	var dfs func(int) bool
	dfs = func(c int) bool {
		if taken[c] {
			return false
		}

		if checkLoop[c] {
			return true
		}

		checkLoop[c] = true

		for _, r := range req[c] {
			if dfs(r) {
				return true
			}
		}
		taken[c] = true
		seq = append(seq, c)

		checkLoop[c] = false
		return false
	}

	// take course
	for i := 0; i < numCourses; i++ {
		looped := dfs(i)
		if looped {
			return []int{}
		}
	}
	return seq
}
