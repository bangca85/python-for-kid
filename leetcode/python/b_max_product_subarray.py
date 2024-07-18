'''
Bài toán: Tìm dãy con có tích lớn nhất (Maximum Product Subarray)
Vấn đề:
Cho một mảng các số nguyên (có thể bao gồm cả số âm), hãy viết một hàm để tìm tích lớn nhất của một dãy con liên tiếp trong mảng.

Ví dụ:
Input: [2, 3, -2, 4]

Output: 6 (vì dãy con liên tiếp có tích lớn nhất là [2, 3])

Input: [-2, 0, -1]

Output: 0 (vì dãy con liên tiếp có tích lớn nhất là [0])


'''

def maxProductSubarray(arr):
    if not arr:
        return 0

    max_current = min_current = max_global = arr[0]
    for i in range(1, len(arr)):
        temp_max = max(arr[i], max_current * arr[i], min_current * arr[i])
        min_current = min(arr[i], max_current * arr[i], min_current * arr[i])
        max_current = temp_max
        max_global = max(max_global, max_current)
    return max_global

 
arr = [2, 3, -2, 4]
result = maxProductSubarray(arr)
print("Maximum product subarray is:", result)
