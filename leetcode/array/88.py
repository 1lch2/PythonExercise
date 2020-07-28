# 给你两个有序整数数组 nums1 和 nums2，
# 请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#  
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]

from typing import List

# 双指针，从后向前，替换规则类似快排
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        p = len(nums1) - 1

        # 下标不为负，需要包括 0 在内
        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                # 若 nums1 当前位置数比 nums2 大，则交换nums1的数
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        
        # 可能存在 nums1 已经交换完，但是nums1当前数字比nums2最大数字要大
        # 此时 i 已经指向了负数，而 j 尚未遍历完
        # nums1 此时剩下 j 个位置等待填入 （不能使用 p）
        nums1[:j+1] = nums2[:j+1]