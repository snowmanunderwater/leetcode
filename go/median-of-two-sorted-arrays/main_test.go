package main

import "testing"

type testpair struct {
	num1    []int
	num2    []int
	average float64
}

var tests = []testpair{
	{[]int{1, 2}, []int{3, 4}, 2.5},
	{[]int{}, []int{3}, 3},
	{[]int{3}, []int{4}, 3.5},
	{[]int{2, 3, 4, 5}, []int{}, 3.5},
	{[]int{2, 3}, []int{}, 2.5},
}

func TestFindMedianSortedArrays(t *testing.T) {
	for _, pair := range tests {
		v := FindMedianSortedArrays(pair.num1, pair.num2)
		if v != pair.average {
			t.Error(
				"For", pair.num1, pair.num2,
				"expected", pair.average,
				"got", v,
			)
		}
	}
}
