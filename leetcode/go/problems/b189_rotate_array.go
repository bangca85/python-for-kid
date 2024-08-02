/*
https://leetcode.com/problems/rotate-array/description/

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
*/
package problems

import (
	"fmt"
)

// Function to reverse a part of the array
func reverse(nums []int, start int, end int) {
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}

// Function to rotate the array to the right by k steps
func rotate(nums []int, k int) {
	n := len(nums)
	k = k % n // In case k is greater than n

	// Step 1: Reverse the entire array
	reverse(nums, 0, n-1)

	// Step 2: Reverse the first k elements
	reverse(nums, 0, k-1)

	// Step 3: Reverse the remaining n-k elements
	reverse(nums, k, n-1)
}

func TestRotate() {
	nums1 := []int{1, 2, 3, 4, 5, 6, 7}
	k1 := 3
	rotate(nums1, k1)
	fmt.Println(nums1)

	nums2 := []int{-1, -100, 3, 99}
	k2 := 2
	rotate(nums2, k2)
	fmt.Println(nums2)
}
