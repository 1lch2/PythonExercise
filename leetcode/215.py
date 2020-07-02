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