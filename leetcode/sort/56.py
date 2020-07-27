# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 示例 2:
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

from typing import List

# Original: Time: 8.01%, Memory: 100%
# Using sort(): Time: 65%, Memory: 93.75%
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        # 按左端点排序
        # self.qsort(intervals, 0, len(intervals)-1) # 自写慢速
        intervals.sort(key=lambda x: x[0]) # 库函数满速

        i = 0
        l = len(intervals)
        while i < l - 1:
            current = intervals[i]
            nextt = intervals[i+1]

            # 分情况讨论区间
            if nextt[0] >= current[0] and nextt[0] <= current[1] and nextt[1] > current[1]:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [current[0], nextt[1]])
            elif current[0] <= nextt[0] and current[1] >= nextt[1]:
                intervals.pop(i+1)
            elif nextt[1] <= current[1] and nextt[1] >= current[0] and nextt[0] < current[0]:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [nextt[0], current[1]])
            else:
                i += 1

            l = len(intervals)

        return intervals

    
    def qsort(self, seq, low, high):
        i = low
        j = high

        if low < high:
            base = seq[i]

            while i < j:
                while seq[j][0] > base[0] and i < j:
                    j -= 1
                if i < j:
                    seq[i] = seq[j]
                    i += 1
                while seq[i][0] < base[0]  and i < j:
                    i += 1
                if i < j:
                    seq[j] = seq[i]
                    j -= 1
            
            seq[i] = base

            self.qsort(seq, low, i-1)
            self.qsort(seq, i+1, high)
