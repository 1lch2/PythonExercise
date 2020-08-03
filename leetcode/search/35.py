# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1

# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4

# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high: # 左右指针交叉后截止
            middle = (high + low) // 2

            if target < nums[middle]:
                high = middle - 1
            elif target > nums[middle]:
                low = middle + 1
            elif target == nums[middle]:
                return middle
        
        # 若目标不在列表中
        if nums[middle] >= target: 
            return middle
        else:
            return middle+1
