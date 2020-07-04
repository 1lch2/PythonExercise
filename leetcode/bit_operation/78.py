from typing import List


# Binary bits solution.
# Reference: http://wuchong.me/blog/2014/07/28/permutation-and-combination-realize/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allset = []
        l_len = len(nums)

        n = 1 << l_len
        for i in range(1, n):
            t_list = []
            for j in range(l_len):
                temp = i
                if temp & (1 << j):
                    t_list.append(nums[j])

            allset.append(t_list)

        allset.append([])
        return allset
