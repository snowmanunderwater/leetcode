// https://leetcode.com/problems/reverse-integer/

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	fmt.Print(reverse(312))
}

func reverse(num int) int {

	if num > 0 {
		s := strconv.Itoa(num)
		runes := []rune(s)
		for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
			runes[i], runes[j] = runes[j], runes[i]
		}
		res := strings.TrimLeft(string(runes), "0")
		n, _ := strconv.Atoi(res)
		if float64(n) > math.Pow(2, 31)-1 || float64(n) < -(math.Pow(2, 31)) {
			return 0
		}
		return n
	}

	s := strconv.Itoa(num)
	runes := []rune(s[1:])
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	res := "-" + strings.TrimLeft(string(runes), "0")
	n, _ := strconv.Atoi(res)
	if float64(n) > math.Pow(2, 31)-1 || float64(n) < -(math.Pow(2, 31)) {
		return 0
	}
	return n

}
