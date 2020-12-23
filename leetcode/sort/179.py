# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

# 示例 1:
# 输入: [10,2]
# 输出: 210

# 示例 2:
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = self.bubble_sort_mod(nums)
        
        return "".join([str(x) for x in nums]) if nums[0] != 0 else "0"

    
    def compare(self, a: int, b: int) -> bool:
        """比较两个数交换前后所得的数字的大小
        """
        return str(a) + str(b) < str(b) + str(a)

    def bubble_sort_mod(self, nums: List[int]) -> List[str]:
        """利用冒泡排序的原理对输入序列进行字典排序
        """
        flag = True
        while flag:
            flag = False
            i = 0
            while i < len(nums) - 1:
                if self.compare(nums[i], nums[i+1]):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    flag = True
                i += 1
        return nums