# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，
# 你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

# 示例 1:
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]

# 示例 2:
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

from typing import List

# Time: 10%, Memory: 100%
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and not newInterval:
            return []
        if not newInterval:
            return intervals

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0]) 

        # Same code as 56.
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


# Time: 45%, Memory: 100%
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and not newInterval:
            return []
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        i = self.binsearch(intervals, newInterval)

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


    def binsearch(self, seq: List[List[int]], target: List[int]) -> int:
        if target[0] > seq[len(seq)-1][0]:
            seq.append(target)
        if target[0] < seq[0][0]:
            seq.insert(0, target)

        low = 0
        high = len(seq) - 1
        l = high - low + 1
        mid = (low + high) // 2
        while l > 1:
            if target[0] < seq[mid][0]:
                high = mid
            elif target[0] > seq[mid][0]:
                low = mid
            elif target[0] == seq[mid][0]:
                seq.insert(mid+1, target)
                return mid
            
            l = high - low
            mid = (low + high) // 2

        if seq[mid][0] > target[0]:
            seq.insert(mid, target)
        else:
            seq.insert(mid+1, target)
        return mid

if __name__ == "__main__":
    intervals = [[2,3],[4,5]]
    newInterval = [0,3]
    S = Solution2()
    # print(S.binsearch(intervals, newInterval))
    # print(intervals)
    print(S.insert(intervals, newInterval))