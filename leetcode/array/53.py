# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 进阶:
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

from typing import List

# https://leetcode-cn.com/problems/maximum-subarray/solution/huan-mei-you-nong-dong-jiu-kan-zhe-yi-pian-ti-jie-/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        global_max = nums[0]
        last_max = nums[0]

        # Choose the bigger sub-sequence and compare it with the current single number.
        # Starting from the second element.
        for i in range(1, len(nums)):
            # if nums[i] + last_max > nums[i], choose the sub-sequence
            if last_max > 0:
                last_max += nums[i]
            # else choose the single number.
            else:
                last_max = nums[i]
            
            # save the global maxmium.
            global_max = max(global_max, last_max)

        return global_max
