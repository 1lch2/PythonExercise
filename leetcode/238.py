from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        l_len = len(nums)
        left = [0 for _ in range(l_len)]
        left[0] = 1
        right = [0 for _ in range(l_len)]
        right[-1] = 1

        # Calculate left side of the index.
        for i in range(l_len-1):
            left[i+1] = left[i] * nums[i]

        # Calculate right side of the index.
        for i in range(l_len-1, 0, -1):
            right[i-1] = right[i] * nums[i]
        
        for i in range(l_len):
            res.append(left[i] * right[i])
        
        return res
