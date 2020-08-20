# 给定一个数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 

# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []
        
        candidates.sort()

        res = []
        used = [False for _ in range(len(candidates))]

        def backtrack(path: list, candidates: list, used: list):
            if sum(path) == target:
                res.append(path.copy())
                return 

            # 需要先判断候选是否为空，不然下一个递归结束条件会出错
            if candidates == []:
                return 

            if sum(path) + min(candidates) > target:
                return 
            
            for i in range(len(candidates)):
                # 跳过不符合要求的元素
                if sum(path) + candidates[i] > target:
                    continue
                
                # 跳过已经使用过的元素
                if used[i]: 
                    continue
                
                # 跳过上一轮迭代选择的相同元素
                if i > 0:
                    if candidates[i] == candidates[i-1] and not used[i]:
                        continue

                used[i] = True
                path.append(candidates[i])
                # 在本次选择之后的元素中进入下一层递归，同时对 used 数组做出同样调整
                backtrack(path, candidates[i+1:], used[i+1:]) 

                used[i] = False
                path.pop()
        
        backtrack([], candidates, used)
        return res

if __name__ == "__main__":
    S = Solution()
    print(S.combinationSum2([10,1,2,7,6,1,5], 8))