/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
*/
package problems

import "fmt"

func canJump(nums []int) bool {
	maxReach := 0 // Biến lưu vị trí xa nhất có thể tới được

	for i := 0; i < len(nums); i++ {
		if i > maxReach { // Nếu vị trí hiện tại vượt quá maxReach, nghĩa là không thể đi tiếp
			return false
		}
		maxReach = max(maxReach, i+nums[i]) // Cập nhật maxReach
		if maxReach >= len(nums)-1 {        // Nếu maxReach đã đến hoặc vượt quá vị trí cuối cùng
			return true
		}
	}

	return true // Nếu duyệt hết mà không bị chặn lại, trả về True
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func TestCanJump() {
	// Ví dụ 1
	nums1 := []int{2, 3, 1, 1, 4}
	fmt.Println(canJump(nums1)) // Output: true

	// Ví dụ 2
	nums2 := []int{3, 2, 1, 0, 4}
	fmt.Println(canJump(nums2)) // Output: false
}
