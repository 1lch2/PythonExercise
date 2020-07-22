# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:

# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortedlist = nums.copy()

        def quicksort(seq, low, high):
            i = low
            j = high
            
            if low < high:
                base = seq[low]
                while i < j:
                    while seq[j] > base and j > i:
                        j -= 1
                    if j > i:
                        seq[i] = seq[j]
                        i += 1
                    
                    while seq[i] < base and i < j:
                        i += 1
                    if i < j:
                        seq[j] = seq[i]
                        j -= 1
                    
                seq[i] = base

                quicksort(seq, low, i-1)
                quicksort(seq, i+1, high)

        quicksort(sortedlist, 0, len(sortedlist)-1)
        res = list(set(sortedlist))

        '''
        或者直接用sort()方法，比自己写的快十倍
        '''
        return res[-k]

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序思路，只排 k 个
        # 还是比快排慢
        def maxHeap(seq: list, size: int, i: int):
            largest = i
            l = 2*i + 1
            r = 2*i + 2

            if l < size and seq[l] > seq[largest]:
                largest = l
            if r < size and seq[r] > seq[largest]:
                largest = r
            if largest != i:
                seq[largest], seq[i] = seq[i], seq[largest]
                maxHeap(seq, size, largest)
        
        n = len(nums)
        for i in range(n, -1, -1):
            maxHeap(nums, n, i)
        
        for i in range(n-1, n-k-1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            maxHeap(nums, i, 0)
        return nums[-k]

class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快排思路，每次确定一个元素的位置
        l = len(nums)
        left = 0
        right = l - 1 
        pivot = self.__partition(nums, 0, l-1)
        while pivot != l - k: 
            pivot = self.__partition(nums, left, right)
            if pivot > l - k: # 若目标在枢轴左侧，则进入左子区间继续一轮快排
                right = pivot - 1
            else:
                left = pivot + 1
        return nums[pivot]

    def __partition(self, seq: list, low: int, high: int):
        i = low
        j = high

        base = seq[i]
        while i < j:
            while seq[j] > base and i < j:
                j -= 1
            if i < j:
                seq[i] = seq[j]
                i += 1
            while seq[i] < base and i < j:
                i += 1
            if i < j:
                seq[j] = seq[i]
                j -= 1
        seq[i] = base
        return i
