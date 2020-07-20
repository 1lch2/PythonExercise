# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间（常数空间）来实现吗？

# 示例 1:
# 输入: [2,2,3,2]
# 输出: 3

# 示例 2:
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

# https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        # 所有位计算规则相同，只对某一位做统计计算
        # two, one 分别为状态转移中两个位的值
        two, one = 0, 0 
        for n in nums:
            one = (one ^ n) & ~two
            two = (two ^ n) & ~one
        
        return one
    