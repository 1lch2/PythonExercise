# 给定一个无重复元素的数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 

# 示例 1：
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]

# 示例 2：
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# 提示：
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []
        
        res = []

        def backtrack(path: list, candidates: list):
            # 递归终止条件 1：已经达到要求
            if sum(path) == target:
                res.append(path.copy()) # 将路径加入结果
                return

            # 递归终止条件 2：候选为空:
            if candidates == []:
                return

            # 递归终止条件 3：当前无有效选择能满足要求
            if sum(path) + min(candidates) > target:
                return
            
            for i in range(len(candidates)):
                if candidates[i] + sum(path) > target: # 跳过使目标不成立的候选
                    continue
                
                path.append(candidates[i])
                backtrack(path, candidates[i:]) # 下一层递归中只能用当前及之后的元素
                path.pop()

        backtrack([], candidates)
        return res

if __name__ == "__main__":
    S = Solution()
    print(S.combinationSum([2,3,5], 8))