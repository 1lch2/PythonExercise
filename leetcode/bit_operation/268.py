# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，
# 找出 0 .. n 中没有出现在序列中的那个数。

# 示例 1:
# 输入: [3,0,1]
# 输出: 2

# 示例 2:
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
#  
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < len(nums):
            # 0 ^ 1 ^ 2 ^ ... ^ k ^ ... ^ n
            # 0 ^ 1 ^ 2 ^ ... ^ _ ^ ... ^ n

            # x ^ x = 0
            # x ^ 0 = x
            # 两次全部异或后会得到缺失的 k
            n = n ^ (i ^ nums[i]) # 此步覆盖掉 n 的初始值
            i += 1
        return n