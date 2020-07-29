# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
# 同时保持非零元素的相对顺序。

# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 说明:
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

from typing import List

# 巨慢的冒泡排序
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        while flag:
            flag = False
            i = 0
            while i + 1 < len(nums):
                if nums[i] == 0 and nums[i+1] != 0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    flag = True
                i += 1

# 仿快排
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        # 以 0 为枢轴，从左向右扫描
        i, j = 0, 0
        # 定位到 0 的下标
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                j += 1
            else:
                break
        while i < len(nums):
            # i 从左向右扫描到不为 0 的数
            while i < len(nums):
                if nums[i] == 0:
                    i += 1
                else:
                    break
            # 交换 0 和不为 0 的数
            # 交换后，i，j，各向后移一位
            if i < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
