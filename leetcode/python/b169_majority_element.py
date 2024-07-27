
def majorityElement(nums):
    candidate = None
    count = 0

    # Candidate selection
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Candidate verification
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No valid majority element found")

# Example usage:
nums1 = [3, 2, 3]
print(majorityElement(nums1))  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums2))  # Output: 2
