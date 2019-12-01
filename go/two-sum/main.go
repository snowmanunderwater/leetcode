// https://leetcode.com/problems/two-sum/

package main

import "fmt"

func main() {
	fmt.Println(twoSum([]int{3, 3}, 6))
}

func twoSum(nums []int, target int) []int {
	result := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		key := target - nums[i]
		v, ok := result[key]
		if ok {
			return []int{v, i}
		}
		result[nums[i]] = i

		key = target - nums[i]
		v, ok = result[key]

		if ok && (i != v) {
			return []int{v, i}
		}
	}
	return []int{}
}
