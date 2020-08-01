# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]

# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]

# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。

# 进阶：
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，
# 并且你不能一次加载所有的元素到内存中，你该怎么办？

from typing import List
import collections

# 求的不是按顺序的交集，是元素单独的带重复交集

# Credit: LeetCode/RUMIF
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 数两个数组中元素的个数，以元素为键，个数为值存入dict
        # 取两个dict的相同键的项的最小值
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return num.elements()

# 排序后求交集
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.qsort(nums1, 0, len(nums1)-1)
        self.qsort(nums2, 0, len(nums2)-1)

        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res


    # Quick sort
    def qsort(self, seq: list, low: int, high: int):
        i = low
        j = high

        if low < high:
            base = seq[i]
            while i < j:
                while i < j and seq[j] > base:
                    j -= 1
                if i < j:
                    seq[i] = seq[j]
                    i += 1

                while i < j and seq[i] < base:
                    i += 1
                if i < j:
                    seq[j] = seq[i]
                    j -= 1

            seq[i] = base
            self.qsort(seq, low, i-1)
            self.qsort(seq, i+1, high)
