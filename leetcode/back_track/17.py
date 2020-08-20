# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

#  1      2       3
#        ABC     DEF 

#  4      5       6
# GHI    JKL     MNO

#  7      8       9
# PQRS   TUV     WXYZ


# 示例:
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        charMap = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}
        
        digits = list(digits)
        res = []

        def backtrack(path: str, selection: str):
            # 递归终止条件：当候选数字为空时
            if len(selection) == 0:
                res.append(path)
                return
            
            # 对当前数字对应的所有可能字母进行遍历
            for char in charMap[selection[0]]:
                path += char

                backtrack(path, selection[1:]) # 去除当前选择的数字，进入下一层递归

                path = path[:-1]
        
        backtrack("", digits)
        return res
