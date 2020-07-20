# 给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        # O(n^2)       
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]

# https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i