from typing import List

# https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/
class Solution0:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp_list = nums.copy()
        l_len = len(nums)

        def dfs(path, depth, length, res, queue, used):
            if depth == length:
                res.append(path.copy()) # Make a copy of `path` to prevent `res` from being changed when `path` changes.
                return 
            for i in range(l_len):
                if used[i] == False:
                    used[i] = True
                    path.append(queue.pop(0))

                    dfs(path, depth+1, length, res, queue, used)

                    used[i] = False
                    queue.append(path.pop())
        
        used = [False for _ in range(l_len)]
        dfs([], 0, l_len, res, temp_list, used)

        return res


