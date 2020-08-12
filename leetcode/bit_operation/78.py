# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

from typing import List

# Binary bits solution.
# Reference: http://wuchong.me/blog/2014/07/28/permutation-and-combination-realize/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #* 使用二进制位的迭代来代表对应元素是否在组合中存在
        res = [] # 不需要提前加入空集

        bitmask = 1 # 用来判断对应数字是否加入的掩码
        iter_times = bitmask << len(nums) # 循环截止的上限值

        for i in range(iter_times): # 迭代从 0 开始则第一个加入的是空集
            temp = []
            for j in range(len(nums)): # 在给定元素数量内循环检测每一位是否要加入
                if (1 << j) & i: # 若对应位和掩码与结果不为 0 则加入
                    temp.append(nums[j]) 
            res.append(temp)
        return res
