
from typing import List


def maxSubArray(nums: List[int]) -> int:
        max_total = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                current_total = 0
                for k in range(i, j+1):
                    current_total += nums[k]
                if current_total > max_total:
                    max_total = current_total
            
        return max_total

def main():
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  

if __name__ == "__main__":
    main()
