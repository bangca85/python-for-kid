'''
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
 
'''

def reverse(nums, start, end):
    """
    Reverse the elements of the list nums from index start to end.
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums, k):
    """
    Rotate the elements of the list nums to the right by k steps.
    """
    n = len(nums)
    if n == 0 or k <= 0:
        return

    k = k % n  # Handle cases where k is greater than the length of nums

    # Step 1: Reverse the entire array
    reverse(nums, 0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Step 3: Reverse the remaining n - k elements
    reverse(nums, k, n - 1)

def rotateCyclic(nums, k):
    """
    Rotate the elements of the list nums to the right by k steps. Cyclic Replacements Implementation.
    """
    n = len(nums)
    k = k % n
    count = 0
    start = 0
    
    while count < n:
        current = start
        prev = nums[start]
        
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            
            if start == current:
                break
        
        start += 1


# Example usage
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    rotate(nums1, k1)
    print("Rotated array:", nums1)   
    # Example 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    rotate(nums2, k2)
    print("Rotated array:", nums2)   

    # Example 3: Edge case where k is 0
    nums3 = [1, 2, 3]
    k3 = 0
    rotate(nums3, k3)
    print("Rotated array:", nums3)   

    # Example 4: Edge case where nums is empty
    nums4 = []
    k4 = 4
    rotate(nums4, k4)
    print("Rotated array:", nums4)   

    # Example 5: Edge case where k is greater than the length of nums
    nums5 = [1, 2, 3, 4, 5, 6, 7]
    k5 = 10
    rotate(nums5, k5)
    print("Rotated array:", nums5) 
