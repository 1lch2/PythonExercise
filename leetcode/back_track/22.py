# 数字 n 代表生成括号的对数，
# 请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 示例：
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []

        charMap = [1, 0] # 记录左右括号的数量
        res = []

        def backtrack(path: str, charMap: dict):
            if len(path) == 2*n:
                res.append(path)
                return
            
            # 左侧进入条件
            if charMap[0] < n:
                charMap[0] += 1
                path += "("
                backtrack(path, charMap)

                path = path[:-1]
                charMap[0] -= 1
            
            # 右侧进入条件
            if charMap[1] < charMap[0]:
                charMap[1] += 1
                path += ")"
                backtrack(path, charMap)

                path = path[:-1]
                charMap[1] -= 1


        backtrack("(", charMap)
        return res

if __name__ == "__main__":
    S = Solution()
    print(S.generateParenthesis(3))