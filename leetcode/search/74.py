# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 示例 1：
# 输入：matrix = [[1,3,5,7],
#                 [10,11,16,20],
#                 [23,30,34,50]], target = 3
# 输出：true

# 示例 2：
# 输入：matrix = [[1,3,5,7],
#                 [10,11,16,20],
#                 [23,30,34,50]], target = 13
# 输出：false

# 示例 3：
# 输入：matrix = [], target = 0
# 输出：false
#  
# 提示：
# m == matrix.length
# n == matrix[i].length
# 0 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

# Time: 60%
# O(mlogn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for row_index in range(len(matrix)):
            current_row = matrix[row_index]
            # 目标在一行内
            if target >= current_row[0] and target <= current_row[-1]:
                return self.bin_search(current_row, target)
            else:
                if row_index < len(matrix) -1:
                    # 目标在两行之间
                    if target > current_row[-1] and target < matrix[row_index+1][0]:
                        return False


    def bin_search(self, nums: List[int], target: int) -> bool:
        """Binary search without returning target index.
        """
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False