package problems

import (
	"fmt"
)

func majorityElement(nums []int) int {
	var candidate int
	count := 0

	// Candidate selection phase
	for _, num := range nums {
		if count == 0 {
			candidate = num
		}
		if num == candidate {
			count++
		} else {
			count--
		}
	}

	// Candidate verification phase
	count = 0
	for _, num := range nums {
		if num == candidate {
			count++
		}
	}

	if count > len(nums)/2 {
		return candidate
	} else {
		panic("No valid majority element found")
	}
}

func TestMajorityElement() {
	// Example usage
	nums1 := []int{3, 2, 3}
	fmt.Println(majorityElement(nums1)) // Output: 3

	nums2 := []int{2, 2, 1, 1, 1, 2, 2}
	fmt.Println(majorityElement(nums2)) // Output: 2
}
