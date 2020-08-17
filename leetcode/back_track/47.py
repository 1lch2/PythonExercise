# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 同一层之间迭代，不同层之间递归向下进入
        #     "112"
        #     / | \
        #   1   1   2
        #  / \     / \
        # 1  2    1   1
        # |  |    |
        # 2  1    1
        
        if not nums:
            return []

        # 元素需要先排序后续才能使用假设  
        nums.sort()

        res = []
        used = [False for _ in range(len(nums))]

        def backtrack(path: list, selection: list):
            # 递归终止：可用选项只有一个
            if used.count(False) == 0:
                res.append(path.copy()) # 使用拷贝避免引用导致结果被修改
                return
            
            # 遍历可用选择
            for index in range(len(selection)):
                # 若当前选项已被选择过则跳过
                if not used[index]:                
                # 若当前选择与上一轮选择的元素相同则跳过
                    if index > 0:
                        # index 下标无法区分不同递归，需要判断前一次是否被选择过
                        # 若相同元素在前一次递归被选择过则需要剪枝
                        # 使用跨越不同层递归的 used 来判断
                        if selection[index] == selection[index-1] and not used[index-1]:
                            continue
                    
                    used[index] = True
                    path.append(selection[index])
                    backtrack(path, selection)

                    path.pop()
                    used[index] = False
        
        backtrack([], nums)

        return res

def main():
    S = Solution()
    l = [1,1,2]
    print(S.permuteUnique(l))

if __name__ == "__main__":
    main()