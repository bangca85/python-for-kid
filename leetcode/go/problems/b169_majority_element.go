/*
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
*/
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
