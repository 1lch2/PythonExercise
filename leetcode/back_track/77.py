# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k < 1:
            return []

        selection = [i for i in range(1, n+1)] # 选项
        res = []

        def backtrack(start: int, path: list, selection: list):
            # 递归终止：path 已经有指定数量的元素k
            if len(path) == k:
                res.append(path[:]) # 使用拷贝避免引用导致结果被修改
                return
            
            # 遍历可用选择
            for i in range(start, n):                
                path.append(selection[i])

                # 排除本次选择元素，进入下一层递归
                backtrack(i+1, path, selection)

                path.pop() # 删除本次选择元素
        
        backtrack(0, [], selection)
        return res
