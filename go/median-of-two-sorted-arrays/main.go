// https://leetcode.com/problems/median-of-two-sorted-arrays/

package main

import (
	"fmt"
	"sort"
)

func main() {

	fmt.Println(FindMedianSortedArrays([]int{2, 3, 4, 5}, []int{}))
}

func FindMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	result := []int{}
	result = append(nums1, nums2...)

	sort.Ints(result)

	if len(result) == 1 {
		return float64(result[0])
	} else if len(result) == 2 {
		return float64(result[0]+result[1]) / 2.0
	} else if len(result)%2 != 0 {
		sered := len(result) / 2
		return float64(result[sered])
	} else {
		sered := (len(result) / 2) - 1
		d, u := sered, sered+1
		return (float64(result[d]) + float64(result[u])) / 2.0
	}
}
